from langchain.llms.base import LLM
from typing import List
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd

# 🔁 Fake LLM for offline testing
class FakeLLM(LLM):
    def _call(self, prompt: str, stop: List[str] = None) -> str:
        return "🤖 [Mock LLM response based on your prompt:]\n" + prompt[:300]

    @property
    def _llm_type(self) -> str:
        return "fake-llm"

# 🧾 Load CSV and summarize it
def load_data_summary(csv_path):
    df = pd.read_csv(csv_path)
    summary = df.describe(include='all').to_string()
    return summary

# 🧱 Build the LangChain with FakeLLM
def build_chain():
    with open("prompts/summary_prompt.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["data_summary", "question"],
        template=template
    )

    llm = FakeLLM()
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

# 🔁 Run the query using mock logic
def run_query(csv_path, user_question):
    data_summary = load_data_summary(csv_path)
    chain = build_chain()
    return chain.run({"data_summary": data_summary, "question": user_question})
