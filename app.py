from flask import Flask, render_template, request, jsonify
from jarvis_core import processCommand

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/command", methods=["POST"])
def command():
    user_command = request.json.get("command")
    response = processCommand(user_command)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
