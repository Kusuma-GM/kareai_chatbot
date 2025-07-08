# 🤖 KareAI MCP Chatbot

A smart chatbot that connects to an MCP (Model Context Protocol) server and fetches real-time data in a human-friendly way — powered by OpenRouter LLMs and a Streamlit interface.

---

## 🔍 Project Overview

This chatbot simulates an intelligent assistant that:

- 🔗 Connects to an MCP server (e.g., Firecrawl or JSONPlaceholder)
- 📥 Fetches structured data from the MCP API
- 🧠 Summarizes and explains the response using an LLM
- 🧾 Displays results in plain English via a chatbot interface

---

## 🧰 Tech Stack

| Layer     | Tech Used                         |
|-----------|-----------------------------------|
| 💬 LLM     | OpenRouter (Free GPT/Claude models) |
| 🧠 MCP API | Firecrawl or JSONPlaceholder      |
| 🖥 Frontend| Streamlit                         |
| 🔁 Backend | Python (requests, dotenv, etc.)   |

---

## ⚙️ Folder Structure

kareai_chatbot/
│
├── backend/
│ ├── main.py # Flask or API layer (optional)
│ ├── mcp_client.py # Connects to MCP server
│ ├── llm_processor.py # Summarizes data using OpenRouter
│ └── requirements.txt # Dependencies
│
├── frontend/
│ └── streamlit_app.py # Chatbot UI in Streamlit
│
├── MiniMax-MCP-JS/ # MCP server client (optional, for testing)
├── .env # 🔒 Secrets (excluded from Git)
├── .env.example # ✅ Safe reference
├── .gitignore
└── README.md

---

## 🚀 How to Run Locally

 **1. Clone the repo**
git clone https://github.com/Kusuma-GM/kareai_chatbot.git
cd kareai_chatbot

**2. Set up virtual environment**
python -m venv venv
.\venv\Scripts\activate      # On Windows
pip install -r backend/requirements.txt

**3. Set up .env**
Create a .env file in the root:
env
OPENAI_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
MCP_BASE_URL=https://jsonplaceholder.typicode.com/posts
🔐 Never commit this file! Use .env.example for safe sharing.

**4. Start the chatbot**

streamlit run frontend/streamlit_app.py
💡 How It Works
User enters a natural language question.

App sends a GET request to the MCP server.

Raw response is sent to the LLM for summarization.

A clean, human-readable answer is displayed.



**Submission Checklist (Kimmchi)**
 Working chatbot interface ✅
echo "* text=auto" > .gitattributes

 Connected to MCP server (e.g. Firecrawl or JSONPlaceholder) ✅

 Summarizes response using LLM ✅

 All code uploaded to GitHub ✅

 

**📬 Contact**
For any help or feedback, feel free to reach out at:
📧 gmkusuma619@gmail.com


