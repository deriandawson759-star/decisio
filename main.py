from flask import Flask, request, jsonify
import os

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
    return {"status": "Decisio running"}


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

    if score >= 8:
        level = "Strong Strategic Position"
    elif score >= 6:
        level = "Moderate Strategic Position"
    else:
        level = "Weak Strategic Position"

    report = {
        "company_analysis": {
            "market_strength": market,
            "financial_structure": finance,
            "strategic_positioning": positioning,
            "operational_execution": execution,
            "growth_potential": growth
        },
        "strategic_score": score,
        "classification": level,
        "recommendations": [
            "Improve operational efficiency",
            "Strengthen financial discipline",
            "Leverage market positioning for growth"
        ]
    }

    return jsonify(report)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
