# chain.py
"""
This file contains mock agent logic for summarizing financial data,
detecting risks, and generating final insights for the PennyPilot Hackathon.
"""

def summarize_performance(text):
    """
    Mock financial performance summary agent.
    Simulates analysis of input text (e.g. CSV or financial doc).
    """
    return "Mock Summary: Revenue is stable, growth is moderate, and net profit has improved slightly over the last quarter."


def analyze_risks(text):
    """
    Mock risk and red flag analysis agent.
    Simulates risk scanning based on raw text input.
    """
    return "Mock Risks: Operating costs remain high. Customer retention rate has dropped by 12%. Margins are under pressure."


def generate_final_insights(summary, risks):
    """
    Final agent that merges other agents' outputs into actionable insights.
    """
    return f"""📊 Final Insights for SME:

🔹 Summary:
{summary}

⚠️ Risks & Red Flags:
{risks}

✅ Recommendations:
1. Investigate causes of high operational costs.
2. Launch retention campaign to reduce churn.
3. Consider optimizing pricing or margin structure.
"""