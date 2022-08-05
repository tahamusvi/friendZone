
/**
* Theme: Adminto Admin Template
* Author: Coderthemes
* Dashboard
*/

!function($) {
    "use strict";

    var Dashboard1 = function() {
    	this.$realData = []
    };

    //creates Bar chart
    Dashboard1.prototype.createBarChart  = function(element, data, xkey, ykeys, labels, lineColors) {
        Morris.Bar({
            element: element,
            data: data,
            xkey: xkey,
            ykeys: ykeys,
            labels: labels,
            hideHover: 'auto',
            resize: true, //defaulted to true
            gridLineColor: '#eeeeee',
            barSizeRatio: 0.2,
            barColors: lineColors
        });
    },

    //creates line chart
    Dashboard1.prototype.createLineChart = function(element, data, xkey, ykeys, labels, opacity, Pfillcolor, Pstockcolor, lineColors) {
        Morris.Line({
          element: element,
          data: data,
          xkey: xkey,
          ykeys: ykeys,
          labels: labels,
          fillOpacity: opacity,
          pointFillColors: Pfillcolor,
          pointStrokeColors: Pstockcolor,
          behaveLikeLine: true,
          gridLineColor: '#eef0f2',
          hideHover: 'auto',
          resize: true, //defaulted to true
          pointSize: 0,
          lineColors: lineColors
        });
    },

    //creates Donut chart
    Dashboard1.prototype.createDonutChart = function(element, data, colors) {
        Morris.Donut({
            element: element,
            data: data,
            resize: true, //defaulted to true
            colors: colors
        });
    },
    
    
    Dashboard1.prototype.init = function() {

        //creating bar chart
        var $barData  = [
            { y: '1385', a: 75 },
            { y: '1396', a: 42 },
            { y: '1387', a: 75 },
            { y: '1388', a: 38 },
            { y: '1390', a: 19 },
            { y: '1391', a: 93 }
        ];
        this.createBarChart('morris-bar-example', $barData, 'y', ['a'], ['آمار'], ['#188ae2']);

        //create line chart
        var $data  = [
            { y: '1391', a: 50, b: 0 },
            { y: '1390', a: 75, b: 50 },
            { y: '1391', a: 30, b: 80 },
            { y: '1392', a: 50, b: 50 },
            { y: '1393', a: 75, b: 10 },
            { y: '1394', a: 50, b: 40 },
            { y: '1395', a: 75, b: 50 },
            { y: '1396', a: 100, b: 70 }
          ];
        this.createLineChart('morris-line-example', $data, 'y', ['a','b'], ['سری الف','سری ب'],['0.9'],['#ffffff'],['#999999'], ['#10c469','#188ae2']);

        //creating donut chart
        var $donutData = [
                {label: "دانلودی ها", value: 12},
                {label: "تخفیف ها", value: 30},
                {label: "ایمیل ها", value: 20}
            ];
        this.createDonutChart('morris-donut-example', $donutData, ['#ff8acc', '#5b69bc', "#35b8e0"]);
    },
    //init
    $.Dashboard1 = new Dashboard1, $.Dashboard1.Constructor = Dashboard1
}(window.jQuery),

//initializing 
function($) {
    "use strict";
    $.Dashboard1.init();
}(window.jQuery);