from flask import Flask, request, jsonify

app = Flask(__name__)


def strategic_score(market, finance, positioning, execution, growth):
    score = (
        market * 0.2 +
        finance * 0.2 +
        positioning * 0.2 +
        execution * 0.2 +
        growth * 0.2
    )
    return round(score, 2)


@app.route("/")
def home():
    return {"status": "Decisio AI running"}


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    market = data.get("market", 0)
    finance = data.get("finance", 0)
    positioning = data.get("positioning", 0)
    execution = data.get("execution", 0)
    growth = data.get("growth", 0)

    score = strategic_score(
        market,
        finance,
        positioning,
        execution,
        growth
    )

    result = {
        "market": market,
        "finance": finance,
        "positioning": positioning,
        "execution": execution,
        "growth": growth,
        "strategic_score": score
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
