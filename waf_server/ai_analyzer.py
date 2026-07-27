import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AGENT_ROUTER_KEY") or "dummy-key",
    base_url="https://agentrouter.org/v1"
)

def analyze_payload_with_ai(payload: str, headers: dict) -> dict:
    if not payload and not headers:
        return {"is_threat": False, "threat_type": "Clean", "confidence_score": 0.0, "reasoning": "No payload"}

    prompt = f"""
    Analyze the following HTTP request payload and headers for cyber threats.
    
    Headers: {headers}
    Payload: {payload}

    Categorize threats precisely into ONE of these types if detected:
    - SQL Injection
    - Cross-Site Scripting (XSS)
    - Command Injection
    - Prompt Injection
    - XML External Entity (XXE)
    - NoSQL Injection
    - Server-Side Request Forgery (SSRF)
    - Path Traversal

    Respond ONLY in valid raw JSON with no markdown formatting:
    {{
      "is_threat": true/false,
      "threat_type": "Clean" or "Category Name",
      "confidence_score": 0.0 to 1.0,
      "reasoning": "brief explanation"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content.strip()
        
        # Strip markdown formatting if present
        if content.startswith("```"):
            lines = content.splitlines()
            content = "\n".join(lines[1:-1]) if lines[-1].startswith("```") else "\n".join(lines[1:])
            content = content.replace("json", "").strip()

        data = json.loads(content)
        return {
            "is_threat": bool(data.get("is_threat", False)),
            "threat_type": data.get("threat_type", "Clean" if not data.get("is_threat") else "Anomaly Detected"),
            "confidence_score": float(data.get("confidence_score", 0.0)),
            "reasoning": str(data.get("reasoning", ""))
        }
    except Exception as e:
        print(f"[!] AI Analyzer Error: {e}")
        return {
            "is_threat": False,
            "threat_type": "Clean",
            "confidence_score": 0.0,
            "reasoning": f"Analyzer bypassed: {str(e)}"
        }
