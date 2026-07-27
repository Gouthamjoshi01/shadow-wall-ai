# 🛡️ ShadowWallAI — AI-Aware Web Application Firewall (WAF)

**ShadowWallAI** is a real-time, AI-augmented Web Application Firewall (WAF) designed to detect, classify, and block modern web application attack vectors—including traditional exploits (SQLi, XSS, RCE, LFI, SSRF) and zero-day LLM/AI vulnerabilities (Prompt Injections, Jailbreaks, System Role Overrides).

![ShadowWallAI Interface](https://img.shields.io/badge/Security-AI--WAF-blue?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Language-Python_3.11+-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

---

## ✨ Features

- **Real-Time Threat Intelligence Feed:** WebSocket-driven live stream displaying incoming traffic events instantly without polling.
- **AI-Powered Payload Inspection:** Integrates LLM analysis to evaluate complex payloads and classify subtle anomalies like prompt injections and jailbreaks.
- **Threat Vector Detection:**
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - OS Command Injection (RCE)
  - Path Traversal & Local File Inclusion (LFI)
  - XML External Entity (XXE) Injection
  - Server-Side Request Forgery (SSRF)
  - NoSQL Injection
  - AI / LLM Prompt Injections & Jailbreaks (DAN mode, override attempts)
- **Real-Time Visuals & Analytics:** Live Threat Pulse Oscilloscope, severity tagging (CRITICAL, HIGH, MEDIUM), traffic stats, and payload search filters.
- **Detailed Event Inspector:** Interactive slide-out drawer providing full raw payload examination.

---

## 🏗️ Architecture Overview

                          +------------------------+
                          |   Incoming HTTP Request|
                          +-----------+------------+
                                      |
                                      v
                        +-------------+------------+
                        |   ShadowWallAI WAF Core  |
                        |     (FastAPI Engine)     |
                        +-------------+------------+
                                      |
                  +-------------------+-------------------+
                  |                                       |
                  v                                       v
      +-----------+-----------+               +-----------+-----------+
      |  Static Rule Engine   |               |   LLM / AI Analyzer   |
      | (Regex & Heuristics)  |               | (Context & Anomaly)   |
      +-----------+-----------+               +-----------+-----------+
                  |                                       |
                  +-------------------+-------------------+
                                      |
                                      v
                        +-------------+------------+
                        |  Decision: ALLOW (200)   |
                        |      or BLOCK (403)      |
                        +-------------+------------+
                                      |
                                      v
                        +-------------+------------+
                        | WebSocket Stream Broadcast |
                        +-------------+------------+
                                      |
                                      v
                        +-------------+------------+
                        |  ShadowWallAI Web Dashboard|
                        +--------------------------+

---

## 🚀 Quickstart Guide

### Prerequisites
- Python 3.10+
- Virtualenv

### 1. Repository Setup & Environment
git clone [https://github.com/YOUR_USERNAME/shadowwall-ai.git](https://github.com/YOUR_USERNAME/shadowwall-ai.git)
cd shadowwall-ai

# Activate Virtual Environment
source venv/bin/activate
pip install -r requirements.txt

### 2. Configure Environment Variables
Create a .env file inside waf_server/:
AGENT_ROUTER_KEY=your_llm_api_key_here

### 3. Launch WAF Backend Engine
cd waf_server
uvicorn main:app --reload --port 8000

### 4. Launch Dashboard
In a new terminal window:
cd dashboard
python3 -m http.server 5173

Open http://localhost:5173 in your browser.

### 5. Execute Simulation Suite
In another terminal tab, run the attack testing suite:
python3 test_attacks.py

---

## 📜 License

Distributed under the MIT License. See LICENSE for more information.
