const express = require("express")
const cors = require("cors")
const PDFDocument = require("pdfkit")

const app = express()

app.use(cors())
app.use(express.json())

app.get("/", (req, res) => {
  res.json({ name: "Decisio AI", status: "running" })
})

app.post("/generate-report", (req, res) => {

  const { market, finance, positioning, execution, growth } = req.body

  const score =
    market * 0.2 +
    finance * 0.2 +
    positioning * 0.2 +
    execution * 0.2 +
    growth * 0.2

  const strategicScore = Math.round(score * 10) / 10

  const doc = new PDFDocument()

  res.setHeader("Content-Type", "application/pdf")
  res.setHeader("Content-Disposition", "attachment; filename=report.pdf")

  doc.pipe(res)

  doc.fontSize(24).text("Decisio Strategic Report", { align: "center" })

  doc.moveDown()

  doc.fontSize(14).text(`Market: ${market}`)
  doc.text(`Finance: ${finance}`)
  doc.text(`Positioning: ${positioning}`)
  doc.text(`Execution: ${execution}`)
  doc.text(`Growth: ${growth}`)

  doc.moveDown()

  doc.fontSize(18).text(`Strategic Score: ${strategicScore}/10`)

  doc.end()

})

app.listen(8080, () => {
  console.log("Decisio API running on port 8080")
})

