import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from chain import run_query

# Load OpenAI key from environment
load_dotenv()

# Streamlit page setup
st.set_page_config(page_title="📊 SME Insights Agent", layout="wide")
st.title("📊 SME Insights Agent")
st.markdown("""
Upload your SME financial data as a CSV and ask any question to gain instant AI-generated insights.
""")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    try:
        # Read file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Show a preview
        st.subheader("🔍 Data Preview")
        st.dataframe(df)

        # Save to temp CSV so LangChain can load it
        temp_path = "data/temp_uploaded.csv"
        os.makedirs("data", exist_ok=True)
        df.to_csv(temp_path, index=False)

        # User input for question
        question = st.text_input("💬 Ask a question about this data:")

        if st.button("Get Insight") and question:
            with st.spinner("Thinking..."):
                answer = run_query(temp_path, question)
                st.markdown("### 💡 Insight")
                st.success(answer)

    except Exception as e:
        st.error(f"❌ Error loading CSV: {e}")
else:
    st.info("Please upload a CSV file to get started.")
