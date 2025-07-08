import requests
import os
from dotenv import load_dotenv

load_dotenv()

MCP_BASE_URL = os.getenv("MCP_BASE_URL")

def query_mcp(question):
    try:
        # Get mock data from a public test API
        response = requests.get(f"{MCP_BASE_URL}/1")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"MCP request failed with status {response.status_code}"}
    except Exception as e:
        return {"error": f"MCP request error: {str(e)}"}
