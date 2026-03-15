from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def strategic_engine(market, finance, positioning, execution, growth):

    score = (market + finance + positioning + execution + growth) / 5

    if score >= 8:
        classification = "Strong Strategic Position"
    elif score >= 6:
        classification = "Moderate Strategic Position"
    else:
        classification = "Weak Strategic Position"

    diagnosis = []

    if market < 6:
        diagnosis.append("Market positioning is weak and requires strategic differentiation.")

    if finance < 6:
        diagnosis.append("Financial structure limits strategic flexibility.")

    if execution < 6:
        diagnosis.append("Operational execution needs improvement.")

    if growth < 6:
        diagnosis.append("Growth potential is underdeveloped.")

    if positioning >= 8:
        diagnosis.append("Company benefits from strong strategic positioning.")

    recommendations = []

    if market < 6:
        recommendations.append("Improve market positioning and differentiation.")

    if finance < 6:
        recommendations.append("Strengthen financial discipline and capital allocation.")

    if execution < 6:
        recommendations.append("Optimize operational processes and management structure.")

    if growth < 6:
        recommendations.append("Develop new growth initiatives and expansion opportunities.")

    if score >= 7:
        recommendations.append("Leverage strategic strengths to accelerate expansion.")

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
