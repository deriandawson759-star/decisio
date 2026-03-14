from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"name": "Decisio AI", "status": "running"}

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    market = data.get("market", 0)
    finance = data.get("finance", 0)
    positioning = data.get("positioning", 0)
    execution = data.get("execution", 0)
    growth = data.get("growth", 0)

    score = (market + finance + positioning + execution + growth) / 5

    return jsonify({
        "market": market,
        "finance": finance,
        "positioning": positioning,
        "execution": execution,
        "growth": growth,
        "strategic_score": score
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
