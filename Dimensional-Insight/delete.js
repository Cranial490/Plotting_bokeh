const fs = require("fs");
const { parse } = require("csv-parse");


readStream = fs.createReadStream("./dummyData.csv")
  .pipe(parse({ delimiter: ",", from_line: 2 }));

readStream.on("data", function (row) {
    dataExample.push(row);
  })
  .on("error", function (error) {
    console.log(error.message);
  })
  .on("end", function () {
    console.log(dataExample.length);
  });
