const express = require("express")
const cors = require("cors")

const app = express()

app.use(cors())
app.use(express.json())

app.get("/", (req, res) => {
  res.json({
    name: "Decisio AI",
    status: "running"
  })
})

app.post("/analyze", (req, res) => {

  const { market, finance, positioning, execution, growth } = req.body

  const score =
    market * 0.2 +
    finance * 0.2 +
    positioning * 0.2 +
    execution * 0.2 +
    growth * 0.2

  res.json({
    strategicScore: Math.round(score * 10) / 10
  })

})

const PORT = process.env.PORT || 8080

app.listen(PORT, () => {
  console.log("Decisio API running on port", PORT)
})
