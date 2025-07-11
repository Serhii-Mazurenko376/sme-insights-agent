import pandas as pd


# 🧾 Load CSV and summarize it
def load_data_summary(csv_path):
    df = pd.read_csv(csv_path)
    summary = df.describe(include='all').to_string()
    return summary


# 🔁 Run the query using mock logic
def run_query(file_path, question):
    return (
        f"🧪 (Mocked Insight) You asked: '{question}' "
        f"on file: '{file_path}'. This simulates an AI answer!"
    )
