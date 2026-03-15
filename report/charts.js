function generateChart(data) {

const ctx = document.getElementById("chart")

new Chart(ctx, {

type: "radar",

data: {

labels: [
"Market",
"Finance",
"Positioning",
"Execution",
"Growth"
],

datasets: [

{

label: "Strategic Analysis",

data: [

data.market,
data.finance,
data.positioning,
data.execution,
data.growth

],

borderColor: "blue",
backgroundColor: "rgba(0,0,255,0.2)"

}

]

}

})

}
