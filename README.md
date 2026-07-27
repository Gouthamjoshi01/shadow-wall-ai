# 🛡️ ShadowWallAI — AI-Aware Web Application Firewall (WAF)

[![Security](https://img.shields.io/badge/Security-AI--WAF-blue?style=flat-square)](https://github.com/Gouthamjoshi01/shadow-wall-ai)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat-square)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

**ShadowWallAI** is a real-time, AI-augmented Web Application Firewall (WAF) designed to inspect, classify, and block web attacks—from traditional vulnerabilities (**SQLi, XSS, RCE, LFI, SSRF**) to **LLM/AI threat vectors** (Prompt Injections, System Role Overrides, DAN Jailbreaks).

---

## 📸 Demo Screenshots

| 📊 Live Monitoring Dashboard | ⚡ WAF Engine Logs |
| :---: | :---: |
| ![Dashboard]( />) | ![Backend Logs]() |

<p align="center">
  <b>🧪 Attack Vector Simulation Suite (15+ Test Vectors)</b><br>
  <img src="assets/attack_simulation.png" width="90%" alt="Attack Simulation Suite">
</p>

---

## ✨ Features & Coverage

* ⚡ **WebSocket Live Telemetry**: Real-time traffic streaming to the dashboard without polling overhead.
* 🧠 **Dual-Engine Filtering**: Instant signature matching paired with LLM context analysis for subtle payloads.
* 🎯 **Broad Defense Scope**: Protects against Web Exploits, Auth Bypass, and AI Prompt Injections / Exfiltration.

---

## 🚀 Quick Start

```bash
# 1. Clone Repository
git clone [https://github.com/Gouthamjoshi01/shadow-wall-ai.git](https://github.com/Gouthamjoshi01/shadow-wall-ai.git) && cd shadow-wall-ai

# 2. Start Backend Server (Terminal 1)
source venv/bin/activate
cd waf_server && uvicorn main:app --reload --port 8000

# 3. Serve Frontend Dashboard (Terminal 2)
cd ../dashboard && python3 -m http.server 5173
# 👉 Access UI at http://localhost:5173

# 4. Run Threat Simulation Suite (Terminal 3)
python3 test_attacks.py
