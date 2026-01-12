from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Deployed via GitHub Actions CI/CD on AWS EC2!"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/version")
def version():
    return jsonify(
        version=os.getenv("APP_VERSION", "local"),
        env=os.getenv("ENV", "dev")
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
