import streamlit as st

st.set_page_config(page_title="AI Stock Market Analyzer", layout="wide")

st.title("📈 AI Stock Market Analyzer")
st.write("Welcome to AI Stock Market Analyzer")

stock = st.text_input("Enter Stock Symbol (Example: RELIANCE.NS)", "RELIANCE.NS")

if st.button("Analyze"):
    st.success(f"Analysis started for {stock}")
    st.info("AI Engine will be added in the next step.")