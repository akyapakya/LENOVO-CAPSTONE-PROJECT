
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    response = f"EduMate AI Response: You asked '{msg}'. This is a demo educational response."
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
