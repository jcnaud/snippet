var w = 1600;
var h = 500;

var svg = d3
  .selectAll(".svg")
  //.selectAll("svg")
  .append("svg")
  .attr("width", w)
  .attr("height", h)
  .attr("class", "svg");

var taskArray = [
  {
    task: "Jean Nicoli",
    type: "Margonajo",
    startTime: "2013-1-9 12:10", //year/month/day
    endTime: "2013-1-10 18:24",
    details: "120 vl, 30 er, 350 pax, md "
  },

  {
    task: "Mega Express III",
    type: "Trois Maries N",
    startTime: "2013-1-9 8:24",
    endTime: "2013-1-9 18:24",
    details: "110 vl, 250 pax, md cl3"
  },

  {
    task: "Mega Express II",
    type: "Trois Maries S",
    startTime: "2013-1-6 0:0",
    endTime: "2013-1-9 10:10"
  },

  {
    task: "Girolata",
    type: "Capucins N",
    startTime: "2013-1-2 11:20",
    endTime: "2013-1-3 18:06",
    details: "48 ER"
  },

  {
    task: "Surcouf",
    type: "Capucins S",
    startTime: "2013-1-6 14:25",
    endTime: "2013-1-9 14:35"
  },

  {
    task: "Queen Elisabeth",
    type: "Mole Croisières",
    startTime: "2013-1-9 6:53",
    endTime: "2013-1-12 7:24",
    details: "2350 pax"
  },

  {
    task: "Vega",
    type: "Mole Croisières",
    startTime: "2013-1-12 00:24",
    endTime: "2013-1-14 14:04",
    details: "Inaugurale"
  },
  {
    task: "East Indian Ocean",
    type: "M Croisières",
    startTime: "2013-1-8 1:45",
    endTime: "2013-1-13 3:00",
    details: "L 320 m, l 58 m"
  },

  {
    task: "crying",
    type: "Jeanne d'Arc",
    startTime: "2013-1-13 06:00",
    endTime: "2013-1-16 07:00"
  },

  {
    task: "crying II",
    type: "St Joseph",
    startTime: "2013-1-11 14:35",
    endTime: "2013-1-16 21:00"
  },
  {
    task: "Belouga",
    type: "Mouillage 1",
    startTime: "2013-1-7 8:12",
    endTime: "2013-1-14 9:30"
  }
];

var dateFormat = d3.time.format("%Y-%m-%d %H:%M"); //%Y-%m-%d %H:%M:%S

var timeScale = d3.time
  .scale()
  .domain([
    d3.min(taskArray, function(d) {
      return dateFormat.parse(d.startTime);
    }),
    d3.max(taskArray, function(d) {
      return dateFormat.parse(d.endTime);
    })
  ])
  .range([0, w - 150]);

var categories = new Array();

for (var i = 0; i < taskArray.length; i++) {
  categories.push(taskArray[i].type);
}

var catsUnfiltered = categories; //for vert labels

categories = checkUnique(categories);

makeGant(taskArray, w, h);

var title = svg
  .append("text")
  .text("Gantt Chart Prévisions d'escale")
  .attr("x", w / 2)
  .attr("y", 25)
  .attr("text-anchor", "middle")
  .attr("font-size", 18)
  .attr("fill", "#009FFC");

function makeGant(tasks, pageWidth, pageHeight) {
  var barHeight = 20;
  var gap = barHeight + 4;
  var topPadding = 75;
  var sidePadding = 90;

  var colorScale = d3.scale
    .linear()
    .domain([0, categories.length])
    .range(["#00B9FA", "#F95002"])
    .interpolate(d3.interpolateHcl);

  makeGrid(sidePadding, topPadding, pageWidth, pageHeight);
  drawRects(
    tasks,
    gap,
    topPadding,
    sidePadding,
    barHeight,
    colorScale,
    pageWidth,
    pageHeight
  );
  vertLabels(gap, topPadding, sidePadding, barHeight, colorScale);
}

function drawRects(
  theArray,
  theGap,
  theTopPad,
  theSidePad,
  theBarHeight,
  theColorScale,
  w,
  h
) {
  var bigRects = svg
    .append("g")
    .selectAll("rect")
    .data(theArray)
    .enter()
    .append("rect")
    .attr("x", 0)
    .attr("y", function(d, i) {
      return i * theGap + theTopPad - 2;
    })
    .attr("width", function(d) {
      return w - theSidePad / 2;
    })
    .attr("height", theGap)
    .attr("stroke", "none")
    .attr("fill", function(d) {
      for (var i = 0; i < categories.length; i++) {
        if (d.type == categories[i]) {
          return d3.rgb(theColorScale(i));
        }
      }
    })
    .attr("opacity", 0.2);

  var rectangles = svg
    .append("g")
    .selectAll("rect")
    .data(theArray)
    .enter();

  var innerRects = rectangles
    .append("rect")
    .attr("rx", 3)
    .attr("ry", 3)
    .attr("x", function(d) {
      return timeScale(dateFormat.parse(d.startTime)) + theSidePad;
    })
    .attr("y", function(d, i) {
      return i * theGap + theTopPad;
    })
    .attr("width", function(d) {
      return (
        timeScale(dateFormat.parse(d.endTime)) -
        timeScale(dateFormat.parse(d.startTime))
      );
    })
    .attr("height", theBarHeight)
    .attr("stroke", "none")
    .attr("fill", function(d) {
      for (var i = 0; i < categories.length; i++) {
        if (d.type == categories[i]) {
          return d3.rgb(theColorScale(i));
        }
      }
    });

  var rectText = rectangles
    .append("text")
    .text(function(d) {
      return d.task;
    })
    .attr("x", function(d) {
      return (
        (timeScale(dateFormat.parse(d.endTime)) -
          timeScale(dateFormat.parse(d.startTime))) /
          2 +
        timeScale(dateFormat.parse(d.startTime)) +
        theSidePad
      );
    })
    .attr("y", function(d, i) {
      return i * theGap + 14 + theTopPad;
    })
    .attr("font-size", 11)
    .attr("text-anchor", "middle")
    .attr("text-height", theBarHeight)
    .attr("fill", "#fff");

  rectText
    .on("mouseover", function(e) {
      // console.log(this.x.animVal.getItem(this));
      var tag = "";

      if (d3.select(this).data()[0].details != undefined) {
        tag =
          "Navire: " +
          d3.select(this).data()[0].task +
          "<br/>" +
          "Quai: " +
          d3.select(this).data()[0].type +
          "<br/>" +
          "Accostage: " +
          d3.select(this).data()[0].startTime +
          "<br/>" +
          "Appareillage: " +
          d3.select(this).data()[0].endTime +
          "<br/>" +
          "Observations: " +
          d3.select(this).data()[0].details;
      } else {
        tag =
          "Navire: " +
          d3.select(this).data()[0].task +
          "<br/>" +
          "Quai: " +
          d3.select(this).data()[0].type +
          "<br/>" +
          "Accostage: " +
          d3.select(this).data()[0].startTime +
          "<br/>" +
          "Appareillage: " +
          d3.select(this).data()[0].endTime;
      }
      var output = document.getElementById("tag");

      var x = this.x.animVal.getItem(this) + "px";
      var y = this.y.animVal.getItem(this) + 25 + "px";

      output.innerHTML = tag;
      output.style.top = y;
      output.style.left = x;
      output.style.display = "block";
    })
    .on("mouseout", function() {
      var output = document.getElementById("tag");
      output.style.display = "none";
    });

  innerRects
    .on("mouseover", function(e) {
      //console.log(this);
      var tag = "";

      if (d3.select(this).data()[0].details != undefined) {
        tag =
          "Navire: " +
          d3.select(this).data()[0].task +
          "<br/>" +
          "Quai: " +
          d3.select(this).data()[0].type +
          "<br/>" +
          "Accostage: " +
          d3.select(this).data()[0].startTime +
          "<br/>" +
          "Appareillage: " +
          d3.select(this).data()[0].endTime +
          "<br/>" +
          "Observations: " +
          d3.select(this).data()[0].details;
      } else {
        tag =
          "Navire: " +
          d3.select(this).data()[0].task +
          "<br/>" +
          "Quai: " +
          d3.select(this).data()[0].type +
          "<br/>" +
          "Appareillage: " +
          d3.select(this).data()[0].startTime +
          "<br/>" +
          "Observations: " +
          d3.select(this).data()[0].endTime;
      }
      var output = document.getElementById("tag");

      var x = this.x.animVal.value + this.width.animVal.value / 2 + "px";
      var y = this.y.animVal.value + 25 + "px";

      output.innerHTML = tag;
      output.style.top = y;
      output.style.left = x;
      output.style.display = "block";
    })
    .on("mouseout", function() {
      var output = document.getElementById("tag");
      output.style.display = "none";
    });
}

function makeGrid(theSidePad, theTopPad, w, h) {
  var xAxis = d3.svg
    .axis()
    .scale(timeScale)
    .orient("bottom")
    .ticks(d3.time.days, 1)
    .tickSize(-h + theTopPad + 20, 0, 0)
    .tickFormat(d3.time.format("%d %b"));

  var grid = svg
    .append("g")
    .attr("class", "grid")
    .attr("transform", "translate(" + theSidePad + ", " + (h - 50) + ")")
    .call(xAxis)
    .selectAll("text")
    .style("text-anchor", "middle")
    .attr("fill", "#000")
    .attr("stroke", "none")
    .attr("font-size", 10)
    .attr("dy", "1em");
}

function vertLabels(
  theGap,
  theTopPad,
  theSidePad,
  theBarHeight,
  theColorScale
) {
  var numOccurances = new Array();
  var prevGap = 0;

  for (var i = 0; i < categories.length; i++) {
    numOccurances[i] = [categories[i], getCount(categories[i], catsUnfiltered)];
  }

  var axisText = svg
    .append("g") //without doing this, impossible to put grid lines behind text
    .selectAll("text")
    .data(numOccurances)
    .enter()
    .append("text")
    .text(function(d) {
      return d[0];
    })
    .attr("x", 10)
    .attr("y", function(d, i) {
      if (i > 0) {
        for (var j = 0; j < i; j++) {
          prevGap += numOccurances[i - 1][1];
          // console.log(prevGap);
          return d[1] * theGap / 2 + prevGap * theGap + theTopPad;
        }
      } else {
        return d[1] * theGap / 2 + theTopPad;
      }
    })
    .attr("font-size", 11)
    .attr("text-anchor", "start")
    .attr("text-height", 14)
    .attr("fill", function(d) {
      for (var i = 0; i < categories.length; i++) {
        if (d[0] == categories[i]) {
          //  console.log("true!");
          return d3.rgb(theColorScale(i)).darker();
        }
      }
    });
}

//from this stackexchange question: http://stackoverflow.com/questions/1890203/unique-for-arrays-in-javascript
function checkUnique(arr) {
  var hash = {},
    result = [];
  for (var i = 0, l = arr.length; i < l; ++i) {
    if (!hash.hasOwnProperty(arr[i])) {
      //it works with objects! in FF, at least
      hash[arr[i]] = true;
      result.push(arr[i]);
    }
  }
  return result;
}

//from this stackexchange question: http://stackoverflow.com/questions/14227981/count-how-many-strings-in-an-array-have-duplicates-in-the-same-array
function getCounts(arr) {
  var i = arr.length, // var to loop over
    obj = {}; // obj to store results
  while (i) obj[arr[--i]] = (obj[arr[i]] || 0) + 1; // count occurrences
  return obj;
}

// get specific from everything
function getCount(word, arr) {
  return getCounts(arr)[word] || 0;
}
