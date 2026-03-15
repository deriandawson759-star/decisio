kfrom flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def strategic_engine(market, finance, positioning, execution, growth):

    # pondérations stratégiques
    score = (
        market * 0.25 +
        finance * 0.20 +
        positioning * 0.25 +
        execution * 0.20 +
        growth * 0.10
    )

    # bonus stratégique
    bonus = 0

    if positioning >= 9 and market >= 9:
        bonus += 0.5

    if execution >= 9 and finance >= 8:
        bonus += 0.3

    if growth >= 9:
        bonus += 0.2

    score = min(score + bonus, 10)

    # classification stratégique
    if score >= 9:
        classification = "Dominant Strategic Position"
    elif score >= 8:
        classification = "Strong Strategic Leader"
    elif score >= 6:
        classification = "Moderate Strategic Position"
    else:
        classification = "Weak Strategic Position"

    # diagnostic stratégique
    diagnosis = []

    if market < 6:
        diagnosis.append("Market competitiveness is weak.")

    if finance < 6:
        diagnosis.append("Financial structure limits strategic flexibility.")

    if execution < 6:
        diagnosis.append("Operational execution is inefficient.")

    if growth < 6:
        diagnosis.append("Growth strategy is underdeveloped.")

    if positioning >= 8:
        diagnosis.append("Strong strategic positioning provides competitive advantage.")

    # recommandations
    recommendations = []

    if market < 6:
        recommendations.append("Strengthen market differentiation and positioning.")

    if finance < 6:
        recommendations.append("Improve capital allocation and financial discipline.")

    if execution < 6:
        recommendations.append("Optimize operational processes and leadership structure.")

    if growth < 6:
        recommendations.append("Develop expansion and innovation initiatives.")

    if score >= 8:
        recommendations.append("Leverage strategic strengths to dominate the market.")

    return {
        "strategic_score": round(score,2),
        "classification": classification,
        "diagnosis": diagnosis,
        "recommendations": recommendations,
        "company_analysis": {
            "market_strength": market,
            "financial_structure": finance,
            "strategic_positioning": positioning,
            "operational_execution": execution,
            "growth_potential": growth
        }
    }


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json

    market = data.get("market",0)
    finance = data.get("finance",0)
    positioning = data.get("positioning",0)
    execution = data.get("execution",0)
    growth = data.get("growth",0)

    result = strategic_engine(
        market,
        finance,
        positioning,
        execution,
        growth
    )

    return jsonify(result)


@app.route("/")
def home():
    return {"status":"Decisio Strategic Engine Running"}
