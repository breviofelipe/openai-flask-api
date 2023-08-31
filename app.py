from flask import Flask, request, jsonify
import os
import openai

MODEL = "gpt-3.5-turbo"
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
app.run(debug=True)


@app.route('/ask',methods=['POST'])
def post_ask():
   req_data = request.get_json()
   chat_completion = openai.ChatCompletion.create(model=MODEL,temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    messages=[{"role": "user", "content": req_data['question']}])
   return jsonify(chat_completion)
