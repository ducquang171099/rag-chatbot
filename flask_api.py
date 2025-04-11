from flask import Flask, render_template, request, jsonify
from handler import chatbot_response
from config import APP_CONFIG

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]
    response = chatbot_response(question)

    return jsonify({ "answer": response })

if __name__ == "__main__":
    app.run(debug=APP_CONFIG["DEBUG"], port=APP_CONFIG["PORT"])
