# ui/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.coordinator import CoordinatorAgent

st.title("📄 Agentic RAG Chatbot")

if "coordinator" not in st.session_state:
    st.session_state.coordinator = CoordinatorAgent()

uploaded_files = st.file_uploader("Upload your documents", accept_multiple_files=True)
query = st.text_input("Ask a question about the documents:")

if st.button("Get Answer") and uploaded_files and query:
    answer, context = st.session_state.coordinator.run(uploaded_files, query)

    st.subheader("Answer:")
    st.write(answer)

    st.subheader("Relevant Context:")
    for chunk in context:
        st.markdown(f"- {chunk}")
