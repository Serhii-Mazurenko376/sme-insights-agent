from chain import run_query

csv_path = "data/sme_data.csv"
question = input("Ask something about the SME data: ")

answer = run_query(csv_path, question)
print("\n🔍 Answer:", answer)
