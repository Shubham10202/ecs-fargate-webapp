from flask import Flask, render_template, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "ecs-fargate-webapp",
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.eviron.get("PORT", 5000)))