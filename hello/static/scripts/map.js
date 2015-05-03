/**
 * Created by Sam on 2/8/15.
*/

        $(function(){
           function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
            }

            var csrftoken = getCookie('csrftoken');


            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }
            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
        });

    function layout_map(json_data,zipcode_data)
    {

        //console.log(json_data);
        //console.log(zipcode_data);
        //var jsonData = JSON.parse(json_data);
        var latitude_points = [];
        var longitude_points = [];
        var city_points = [];
        var zipcode_points = [];
        var average_points = [];


        for (var key in json_data)
        {
            if (json_data.hasOwnProperty(key))
            {
                if (key == 'lat')
                {
                    latitude_points.push(json_data[key]);
                }
                if (key == 'long')
                {
                    longitude_points.push(json_data[key]);
                }
                if (key == 'city')
                {
                    city_points.push(json_data[key]);
                }
                if (key == 'zip')
                {
                    zipcode_points.push(json_data[key]);
                }
            }
        }
        var cities = new L.LayerGroup();
        for (var p = 0; p < latitude_points[0].length; p++){
            L.marker([latitude_points[0][p], longitude_points[0][p]]
            ).bindPopup(city_points[0][p].toString() + ' has an average of '
                 + zipcode_data[p].toString()).addTo(cities);
        }
        //L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.').addTo(cities),
        //L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.').addTo(cities),
        //L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.').addTo(cities),
        //L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.').addTo(cities);


        var mbAttr = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                'Imagery © <a href="http://mapbox.com">Mapbox</a>',
            mbUrl = 'https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png';

        var streets  = L.tileLayer(mbUrl, {id: 'examples.map-i875mjb7'}),
            grayscale   = L.tileLayer(mbUrl, {id: 'examples.map-20v6611k'});

       // var streets = L.tileLayer(mbUrl, {id: 'examples.map-i875mjb7'});

        var map = L.map('map', {
            center: [latitude_points[0][0], longitude_points[0][0]],
            zoom: 11,
            layers: [streets, cities]
        });
        /*
        var map = L.map('map', {
            center: [latitude_points[0][0], longitude_points[0][0]],
            zoom: 10,
            layers: [cities]
        });*/
        var baseLayers = {
            "Streets": streets,
            "Grayscale": grayscale

        };
/*
        var baseLayers = {
            "Streets": streets
        };*/
        var overlays = {
            "Cities": cities
        };

        L.control.layers(baseLayers, overlays).addTo(map);
    }


