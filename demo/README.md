# 🧪 Ollama Chat Demo

This is a simple interactive demo that uses a **local Mistral model** via **Ollama** and **LangChain**.

It lets you chat directly with the model from the terminal — no API keys needed!

---

## ✅ Prerequisites

To run this demo, make sure you have the following installed on your system:

### 1. Python
- Version 3.10+ recommended

### 2. Poetry (for dependency management)
- Install from: https://python-poetry.org/docs/#installation

### 3. Ollama
- Download and install from: https://ollama.com/download
- After installing, pull and run the model:

```bash
ollama run mistral
```

---

## ▶️ Run the Demo

### Step 1: Clone the Repository (if you haven’t)

```bash
git clone https://github.com/Serhii-Mazurenko376/sme-insights-agent.git
cd sme-insights-agent
```

### Step 2: Install Python Dependencies

```bash
poetry install
```

### Step 3: Run the Chat

```bash
poetry run python demo/test_ollama_chat.py
```

---

## 💬 How It Works

This script uses:
- `LangChain`
- `ChatOllama` from `langchain_ollama`
- A simple CLI loop for chatting with a local LLM

No OpenAI keys are needed — everything runs locally using `mistral` via `ollama`.

---

## 📎 File Structure

```
demo/
├── test_ollama_chat.py   # The actual script
└── README.md             # You're reading this 🙂
```

---

## 🧠 Use Case

Perfect for:
- Testing local LLMs during development
- Running secure/offline LLM chat
- Future agent integration without relying on cloud models

---

If you get stuck or want to expand this — ping Serhii! 💡
