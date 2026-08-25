 AI SOC Analyst - Security Copilot

An AI-powered Security Operations Center (SOC) assistant that analyzes security logs, detects suspicious activities, and provides incident analysis.

## Overview

AI SOC Analyst is a cybersecurity project that combines anomaly detection and LLM-based reasoning to assist security analysts in identifying potential threats.

The system analyzes security events such as:

- Failed login attempts
- Brute force attacks
- Suspicious file downloads
- Data exfiltration behavior

and generates security alerts with severity levels.

## Architecture

\`\`\`
Security Logs
      |
      v
Log Parser
      |
      v
Detection Engine
      |
      v
Security Agent
      |
      v
Incident Analysis
\`\`\`

## Features

- Security log ingestion
- Automated threat detection
- Brute force detection
- Data exfiltration detection
- Risk classification
- AI-assisted security analysis
- FastAPI-ready architecture

## Detected Threats

### Brute Force Attack

Detection based on repeated failed authentication attempts.

Example:


Multiple failed SSH login attempts
Source IP: 185.20.30.40
Severity: HIGH


### Data Exfiltration

Detection based on abnormal file download behavior.

Example:


5000 files downloaded by admin user
Severity: CRITICAL


## Project Structure


ai-soc-analyst/

├── data/
│ └── logs/
│ └── security_logs.json
│
├── src/
│ ├── parser/
│ │ └── log_parser.py
│ │
│ ├── anomaly/
│ │ └── detector.py
│ │
│ ├── agent/
│ │
│ └── api/
│
├── tests/
│
├── requirements.txt
└── README.md


## Technologies

- Python
- FastAPI
- Machine Learning
- Anomaly Detection
- LLM Security Concepts
- SOC Operations
- Cybersecurity Analytics

## Installation

Clone repository:

```bash
git clone <repository-url>
cd ai-soc-analyst

Create environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
Run Detection Engine
python -m src.anomaly.detector

Example output:

[
  {
    "type": "Brute Force Attack",
    "severity": "HIGH",
    "source_ip": "185.20.30.40"
  },
  {
    "type": "Data Exfiltration",
    "severity": "CRITICAL",
    "user": "admin"
  }
]
Roadmap
 Security log parser
 Rule-based anomaly detection
 LLM security analyst agent
 RAG-based incident investigation
 SIEM integration
 Real-time log streaming
Author

Sajad Naderzadeh

AI Engineer | Cyber AI
