from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd

def load_data_summary(csv_path):
    df = pd.read_csv(csv_path)
    summary = df.describe(include='all').to_string()
    return summary

def build_chain():
    with open("prompts/summary_prompt.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["data_summary", "question"],
        template=template
    )

    llm = OpenAI(temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def run_query(csv_path, user_question):
    data_summary = load_data_summary(csv_path)
    chain = build_chain()
    return chain.run({"data_summary": data_summary, "question": user_question})
