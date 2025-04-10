from flask import Flask, render_template, request, jsonify
from query_data import chatbot_response

# Init Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]
    response = chatbot_response(question)
    print(response)

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
