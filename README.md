<p align="center">
  <img src="docs/Logo PennyPilot.PNG" alt="Logo PennyPilot" width="160"/>
</p>

# 💡 PennyPilot – SME Insights Agent for Finance

[![Hackathon](https://img.shields.io/badge/GenAI%20Hackathon-2025-blueviolet)](https://genai.works/hackathon)
[![LangChain](https://img.shields.io/badge/Built%20with-LangChain-ffca28)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-informational)](https://platform.openai.com/)

**PennyPilot** is an AI-powered assistant that helps small and medium-sized businesses (SMEs) extract clear insights from financial documents — using LangChain, OpenAI, and FastAPI.

---

## 🚀 What It Does

- 🧾 Analyze uploaded income statements, invoices, or finance notes  
- 📊 Summarize financial performance  
- 🚨 Identify red flags or missed opportunities  
- ✅ Suggest next-step actions in plain English  

---

## 🧠 Agent Flow Logic

This app uses a multi-agent architecture to analyze SME financial documents:

1. **Master Agent** – Orchestrates task
2. **Performance Summarizer** – Summarizes key financial trends
3. **Risk Detector** – Identifies red flags or missed opportunities
4. **Action Advisor** – Converts findings into next-step advice

Plain-text task format:
> “Analyze this document, summarize performance, identify risks, and suggest actions.”

See [`docs/agent_flow_logic.md`](docs/agent_flow_logic.md) for full details.

---

## ⚙️ Tech Stack

- Python  
- LangChain  
- OpenAI (GPT-4 / GPT-3.5)  
- FastAPI  
- *(Optional: Streamlit / CSV upload integration)*

---

## 📁 Project Structure
```
/app        → FastAPI application logic
/agents     → LangChain agents & tools
/prompts    → Prompt templates
/data       → Sample input documents
/docs       → Project pitch, logo, and visual assets
```
---

## 👥 Team PennyPilot

| Name               | Role / Focus Area                     | Location        |
|--------------------|---------------------------------------|-----------------|
| Serhii Mazurenko   | PM, Prompt Engineering, Docs          | Sweden          |
| Jing Li            | AI Technologist, SME tooling support  | UK              |
| Wasif Saeed        | (Former) Backend  – stepped away      | Pakistan        |

---

## ✅ Coordination

- 💬 GitHub Issues: for async collaboration  
- 📋 Trello: DM Serhii to join the private board  
- 📎 Project repo: [github.com/Serhii-Mazurenko376/sme-insights-agent](https://github.com/Serhii-Mazurenko376/sme-insights-agent)

---

## ⏰ Hackathon Timeline

- 📝 **Team Registration Deadline:** July 12, 2025  
- 🚀 **Project Submission Deadline:** **Monday, July 14, 2025**

---

## 🤝 Join the Mission

We’re building a useful, agent-powered tool for real businesses — designed for clarity, not complexity.  

Let’s pilot something that makes a difference.  
— **PennyPilot Team**
