# 👇 Add this block at the top
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 👇 Now import from the backend package
from backend.mcp_client import query_mcp
from backend.llm_processor import summarize_response

import streamlit as st

# 🧠 Rest of your chatbot logic
st.set_page_config(page_title="KareAI Chatbot", page_icon="🤖")
st.title("🤖 KareAI MCP Chatbot")
st.markdown("Ask your question below and let the chatbot fetch + summarize the answer.")

query = st.text_input("Your question:")

if st.button("Ask") and query:
    with st.spinner("Querying MCP and summarizing..."):
        mcp_data = query_mcp(query)
        summary = summarize_response(mcp_data)
        st.success(summary)
