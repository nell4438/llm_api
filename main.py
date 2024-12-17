from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = openai.OpenAI(
    # api_key="glhf_a4c7ed88c9100b2bc434749b20239e8c",
    api_key="glhf_8f89aa796b0ba2682f9145780b34f9ad",
    base_url="https://glhf.chat/api/openai/v1",
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        messages = data.get('messages', [])
        
        if not messages:
            messages = [{"role": "system", "content": "You are a helpful assistant."}]
        
        completion = client.chat.completions.create(
            model="hf:meta-llama/Llama-3.3-70B-Instruct",
            messages=messages
        )
        
        assistant_response = completion.choices[0].message.content
        
        return jsonify({
            "response": assistant_response,
            "messages": messages + [{"role": "assistant", "content": assistant_response}]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True, port=5000)