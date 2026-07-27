# 🛡️ ShadowWallAI — AI-Aware Web Application Firewall (WAF)

[![Security](https://img.shields.io/badge/Security-AI--WAF-blue?style=flat-square)](https://github.com/Gouthamjoshi01/shadow-wall-ai)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**ShadowWallAI** is a real-time, AI-augmented Web Application Firewall (WAF) designed to inspect, classify, and block web attacks—ranging from traditional web exploits (**SQLi, XSS, RCE, LFI, SSRF**) to **LLM/AI threat vectors** (Prompt Injections, System Role Overrides, DAN Jailbreaks).

---

## 📸 System Telemetry & Console Demos

| 📊 Live Monitoring Dashboard | ⚡ Backend WAF Logs |
| :---: | :---: |
| ![Dashboard Console](<img width="1920" height="891" alt="shadowall" src="https://github.com/user-attachments/assets/3a6d2e5c-e993-47e8-a13a-6dfd742a4246" />
) | ![Backend Server Logs](assets/Screenshot_2026-07-27_14_10_53.jpg) |

| 🌐 Python Web Server Terminal | 🧪 15+ Vector Threat Simulation Suite |
| :---: | :---: |
| ![Frontend Web Server](assets/Screenshot_2026-07-27_14_11_04.png) | ![Attack Test Suite](assets/Screenshot_2026-07-27_14_11_15.jpg) |

---

## ✨ Features & Defense Coverage

* ⚡ **WebSocket Telemetry**: Real-time traffic streaming directly to the monitoring console without polling.
* 🧠 **Dual-Engine Inspection**: Microsecond signature matching paired with LLM context evaluation.
* 🎯 **Broad Vulnerability Shield**: Blocks traditional OWASP Top 10 vulnerabilities alongside LLM Jailbreaks, Prompt Injections, and Data Exfiltration attempts.

---

## 🚀 Quick Start Guide

```bash
# 1. Clone Repository
git clone [https://github.com/Gouthamjoshi01/shadow-wall-ai.git](https://github.com/Gouthamjoshi01/shadow-wall-ai.git) && cd shadow-wall-ai

# 2. Start WAF Backend Server (Terminal 1)
source venv/bin/activate
cd waf_server && uvicorn main:app --reload --port 8000

# 3. Serve Frontend Dashboard (Terminal 2)
cd ../dashboard && python3 -m http.server 5173
# 👉 Access UI at http://localhost:5173

# 4. Launch Threat Vector Suite (Terminal 3)
python3 test_attacks.py
