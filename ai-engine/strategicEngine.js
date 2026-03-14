function analyzeCompany(data) {

  const score =
    data.market * 0.2 +
    data.finance * 0.2 +
    data.positioning * 0.2 +
    data.execution * 0.2 +
    data.growth * 0.2

  let recommendation = "stable"

  if (score > 7) recommendation = "strong growth potential"
  if (score < 5) recommendation = "strategic risk"

  return {
    strategicScore: score.toFixed(2),
    recommendation
  }

}

module.exports = { analyzeCompany }
