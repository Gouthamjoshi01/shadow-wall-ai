import re

# Regex patterns for common web attack vectors
SQLI_PATTERN = re.compile(r"('|\"|;|\b(OR|AND|UNION|SELECT|INSERT|DELETE|DROP)\b)", re.IGNORECASE)
XSS_PATTERN = re.compile(r"(<script|javascript:|onload=|onerror=)", re.IGNORECASE)
PATH_TRAVERSAL_PATTERN = re.compile(r"(\.\./|\.\.\\)")

def quick_signature_check(payload: str) -> dict:
    if SQLI_PATTERN.search(payload):
        return {"flagged": True, "type": "SQL Injection"}
    if XSS_PATTERN.search(payload):
        return {"flagged": True, "type": "XSS"}
    if PATH_TRAVERSAL_PATTERN.search(payload):
        return {"flagged": True, "type": "Path Traversal"}
    return {"flagged": False, "type": "Clean"}
