from flask import Flask, request, jsonify, Response
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

    return jsonify({
        "market": market,
        "finance": finance,
        "positioning": positioning,
        "execution": execution,
        "growth": growth,
        "strategic_score": score
    })


@app.route("/report", methods=["POST"])
def report():
def report():

    data = request.json

    market = data.get("market", 0)
    finance = data.get("finance", 0)
    positioning = data.get("positioning", 0)
    execution = data.get("execution", 0)
    growth = data.get("growth", 0)

    score = strategic_score(market, finance, positioning, execution, growth)

    html = f"""
    <html>
    <head>
        <title>Decisio Strategic Report</title>
        <style>
            body {{ font-family: Arial; margin:40px; }}
            h1 {{ color:#2c3e50 }}
            .score {{ font-size:28px; margin-top:20px }}
        </style>
    </head>
    <body>

        <h1>Decisio Strategic Report</h1>

        <h2>Company Analysis</h2>

        <ul>
        <li>Market Strength: {market}</li>
        <li>Financial Structure: {finance}</li>
        <li>Strategic Positioning: {positioning}</li>
        <li>Operational Execution: {execution}</li>
        <li>Growth Potential: {growth}</li>
        </ul>

        <div class="score">
        Strategic Score: {score}/10
        </div>

        <h2>Recommendations</h2>

        <ul>
        <li>Improve operational efficiency</li>
        <li>Strengthen financial discipline</li>
        <li>Leverage strategic positioning</li>
        </ul>

    </body>
    </html>
    """

    return Response(html, mimetype="text/html")

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
