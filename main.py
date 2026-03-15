from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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

    report = {
        "company_analysis": {
            "market_strength": market,
            "financial_structure": finance,
            "strategic_positioning": positioning,
            "operational_execution": execution,
            "growth_potential": growth
        },
        "strategic_score": score
    }

    return jsonify(report)


@app.route("/report", methods=["POST"])
def report():

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

    html = f"""
    <html>
    <head>
        <title>Decisio Strategic Report</title>
        <style>
            body {{ font-family: Arial; margin:40px }}
            h1 {{ color:#2c3e50 }}
            .score {{ font-size:28px }}
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

        <h2 class="score">Strategic Score: {score}/10</h2>

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
