import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
print("🔑 API Key from .env:", API_KEY)

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def summarize_response(raw_data):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:8501",   # Optional: For leaderboard
        "X-Title": "KareAI Chatbot",               # Optional: Your app name
    }

    payload = {
        "model": "mistralai/mistral-7b-instruct",  # ✅ FREE, supported by OpenRouter
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes MCP data."
            },
            {
                "role": "user",
                "content": f"Summarize this MCP data: {raw_data}"
            }
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
        result = response.json()

        print("🔍 OpenRouter response:", result)

        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        elif "error" in result:
            return f"OpenRouter Error: {result['error'].get('message', 'Unknown error')}"
        else:
            return f"Unexpected response: {result}"
    except Exception as e:
        return f"Error summarizing: {str(e)}"
