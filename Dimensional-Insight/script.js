const pointColor = '#3585ff'

const margin = {top: 20, right: 15, bottom: 60, left: 70};
const outerWidth = 800;
const outerHeight = 600;
const width = outerWidth - margin.left - margin.right;
const height = outerHeight - margin.top - margin.bottom;

const container = d3.select('.scatter-container');

// Init SVG
const svgChart = container.append('svg:svg')
    .attr('width', outerWidth)
    .attr('height', outerHeight)
    .attr('class', 'svg-plot')
    .append('g')
    .attr('transform', `translate(${margin.left}, ${margin.top})`);

// Init Canvas
const canvasChart = container.append('canvas')
    .attr('width', width)
    .attr('height', height)
    .style('margin-left', margin.left + 'px')
    .style('margin-top', margin.top + 'px')
    .attr('class', 'canvas-plot');

const context = canvasChart.node().getContext('2d');

// Init Scales
// const x = d3.scaleLinear().domain([0, d3.max(dataExample, (d) => d[0])]).range([0, width]).nice();
// const y = d3.scaleLinear().domain([0, d3.max(dataExample, (d) => d[1])]).range([height, 0]).nice();
const x = d3.scaleLinear().domain([0, 10000]).range([0, width]).nice();
const y = d3.scaleLinear().domain([0, 10000]).range([height, 0]).nice();

// Init Axis
const xAxis = d3.axisBottom(x);
const yAxis = d3.axisLeft(y);

// Add Axis
const gxAxis = svgChart.append('g')
    .attr('transform', `translate(0, ${height})`)
    .call(xAxis);

const gyAxis = svgChart.append('g')
    .call(yAxis);

// Add labels
svgChart.append('text')
    .attr('x', `-${height/2}`)
    .attr('dy', '-3.5em')
    .attr('transform', 'rotate(-90)')
    .text('Axis Y');
svgChart.append('text')
    .attr('x', `${width/2}`)
    .attr('y', `${height + 40}`)
    .text('Axis X');

    
const fs = require("fs");
const { parse } = require("csv-parse");

fs.createReadStream("./example.csv")
  .pipe(parse({ delimiter: ",", from_line: 2 }))
  .on("data", function (row) {
    console.log(row);
    // drawPoint(row)
  })
  .on("error", function (error) {
    console.log(error.message);
  })
  .on("end", function () {
    console.log("finished");
  });

// let dataset = {};


// d3.csv("dummyData.csv").then(function(data){
//     drawPoint(data)
//     })
// // Draw on canvas
// // data.forEach( point => {
// //     drawPoint(point);
// // });

function drawPoint(point) {
    console.log(point)
    context.beginPath();
    context.fillStyle = pointColor;
    const px = x(point['X']);
    const py = y(point['Y']);

    context.arc(px, py, 1.2, 0, 2 * Math.PI,true);
    context.fill();
}