from flask import Flask, render_template, request, jsonify
from agent.agent_logic import run_agent

app = Flask(__name__)

import os

@app.route("/files")
def get_files():
    files = os.listdir("test_project")
    return jsonify(files)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run-agent", methods=["POST"])
def run():
    data = request.json
    task = data.get("task")
    file_path = data.get("file_path")

    result = run_agent(task, file_path)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)