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
| <img src="https://github.com/user-attachments/assets/0c0921a5-d0c5-4b08-b1b2-73583d097d70" width="100%" alt="shadowall"> | <img src="https://github.com/user-attachments/assets/c796cb26-9b9b-44ad-932a-4e872ec36be9" width="100%" alt="server"> |
| **🌐 Python Web Server Terminal** | **🧪 15+ Vector Threat Simulation Suite** |
| <img src="https://github.com/user-attachments/assets/f981bc3d-4794-4a54-a2db-c96a659b8499" width="100%" alt="webserver"> | <img src="https://github.com/user-attachments/assets/6a755a44-beac-4edd-b4da-f28fc8185568" width="100%" alt="attack"> |

---

## ✨ Features & Defense Coverage

* ⚡ **WebSocket Telemetry**: Real-time traffic streaming directly to the monitoring console without polling.
* 🧠 **Dual-Engine Inspection**: Microsecond signature matching paired with LLM context evaluation.
* 🎯 **Broad Vulnerability Shield**: Blocks traditional OWASP Top 10 vulnerabilities alongside LLM Jailbreaks, Prompt Injections, and Data Exfiltration attempts.

---

## 🚀 Quick Start Guide

### 1. Clone Repository & Setup Environment
`git clone https://github.com/Gouthamjoshi01/shadow-wall-ai.git && cd shadow-wall-ai`  
`source venv/bin/activate`

### 2. Configure Environment Variables
Create a `.env` file inside the `waf_server` directory and add your API token:  
`cat <<EOF> waf_server/.env`  
`AGENT_ROUTER_KEY=your_actual_api_key_here`  
`EOF`

### 3. Start WAF Backend Server (Terminal 1)
`cd waf_server && uvicorn main:app --reload --port 8000`

### 4. Serve Frontend Dashboard (Terminal 2)
`cd ../dashboard && python3 -m http.server 5173`  
👉 Access UI at **`http://localhost:5173`**

### 5. Launch Threat Vector Suite (Terminal 3)
`python3 test_attacks.py`

---

## 📜 License
Distributed under the **MIT License**.
