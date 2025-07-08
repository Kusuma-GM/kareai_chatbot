from flask import Flask, request, jsonify
from mcp_client import query_mcp
from llm_processor import summarize_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('query')
    raw_data = query_mcp(user_input)
    final_response = summarize_response(raw_data)
    return jsonify({"response": final_response})

if __name__ == '__main__':
    app.run(debug=True)


