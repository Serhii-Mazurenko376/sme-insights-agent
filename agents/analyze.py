from agentos import Agent

def run_agent(input_text: str):
    agent = Agent()
    return agent.run(input_text)

if __name__ == "__main__":
    test_input = "ACME Corp Q1 2025: Revenue $120,000; Expenses $100,000; What are the key insights?"
    result = run_agent(test_input)
    print("🤖 Agent response:\n", result)
