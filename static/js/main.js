async function my_draw() {
    const element = document.querySelector("svg");
    element.innerHTML = "";
    await draw_color("upload_red", "#e74c3c");
    await draw_color("upload_blue", "#3498db");
}

async function draw_color(string, color) {
    const response = await fetch("http://127.0.0.1:80/" + string);
    let data =  await response.json(); // parses JSON response into native JavaScript objects
    data = data["data"];
    console.log(data);
    d3.select("svg").selectAll()
        .data(data)
    .enter().append("circle")
        .attr("r", 3)
        .attr("cx", function(d) { return 5 + 30 + d.x * width / 50; })
        .attr("cy", function(d) { return -5 + 400 - (30 + d.y * height / 50); })
        .style("fill", color);
}

// set the dimensions and margins of the graph
let margin = { top: 10, right: 30, bottom: 30, left: 30 },
width = 460 - margin.left - margin.right,
height = 400 - margin.top - margin.bottom;

let svg = d3.select("#my_dataviz")
   .append("svg")
   .attr("width", width + margin.left + margin.right)
   .attr("height", height + margin.top + margin.bottom)
   .append("g")
   .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Add X axis
let x = d3.scaleLinear().domain([0, 50]).range([0, width]);

svg
   .append("g")
   .attr("transform", "translate(0," + height + ")")
   .call(d3.axisBottom(x));

//Add x-axis label:
// svg
//    .append("text")
//    .attr("transform","translate(" + width / 2 + " ," + (height + margin.top + 30) + ")")
//    .style("text-anchor", "middle")
   // .text("OX");

// Add Y axis
let y = d3.scaleLinear().domain([0, 50]).range([height, 0]);
svg.append("g").call(d3.axisLeft(y));
//Add y-axis label:
// svg
//    .append("text")
//    .attr("transform", "rotate(-90)")
//    .attr("y", -40)
//    .attr("x", 0 - height / 2)
//    .style("text-anchor", "middle")
   // .text("OY");

// my_draw();
setInterval(my_draw, 500);