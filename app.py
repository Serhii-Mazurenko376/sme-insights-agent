import streamlit as st
import pandas as pd
import os

# Try loading .env (won't crash if missing)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from chain import run_query

st.set_page_config(page_title="📊 SME Insights Agent", layout="wide")
st.title("📊 SME Insights Agent")
st.markdown(
    "Upload your SME financial data as a CSV and ask any question "
    "to gain instant AI-generated insights."
)

uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("🔍 Data Preview")
        st.dataframe(df)

        temp_path = "data/temp_uploaded.csv"
        os.makedirs("data", exist_ok=True)
        df.to_csv(temp_path, index=False)

        question = st.text_input("💬 Ask a question about this data:")

        if st.button("Get Insight") and question:
            with st.spinner("Thinking..."):
                answer = run_query(temp_path, question)
                st.markdown("### 💡 Insight")
                st.success(answer)

    except Exception as e:
        st.error(f"❌ Error processing CSV: {e}")
else:
    st.info("Please upload a CSV file to get started.")
