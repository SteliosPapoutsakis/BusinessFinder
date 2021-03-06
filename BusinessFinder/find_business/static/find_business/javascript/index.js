//
// Front end Javascript for index.html file
// @author Stelios Papoutsakis

let lon,lat;

$(document).ready(function() {
	
	// set geo location on first click if withint
	$('#within').click(() => {
		if (!lon || !lat) {
			if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition((position) => {
						lon = position.coords.longitude;
						lat = position.coords.latitude;
						if (map) {
  						  map.setCenter({
								lat: lat,
								lng: lon
							});
						}
					});
				} else {
					alert('Geo location is not support by this browser');
				}
		}
	});

	
	$('#searchButton').click(() => {
		queryBusiness();
	});

	//query to set locations on map
	queryLocations();

});

"use strict";

let map;
let markers=[];
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: 45.5732,
      lng: -122.7276
    },
    zoom: 10
  });
}

/**
 * Querys the backend for matching business
 *
 * @input (json), paramters for query
 * @output (list), list of matching json objects
 */
function queryBusiness() {
	let query = {
		"type": $('#type').val(),
		"search": $('#search').val(),
		"lat": (lat)?lat:45.5732,
		"lon": (lon)?lon:-122.7276,
		"within": (lon || lat)?$('#within').val():0
	};

	$.ajax({
		url: '/find_business/business_query',
		type: 'POST',
		dataType: 'html',
		headers: {
			'X-CSRFToken': csrftoken,
		},
		// on success, replace new html list
		success: (data) => {
			$('#restaurantList').empty();
			$('#restaurantList').append(data);

			
			//query to set locations on map
			queryLocations();
		},
	//	error: (jqXHR, textStatus,errorThrown ) => {
	//		alert('Error: '+errorThrown+'\nStatus:'+jqXHR.status);
	//	},
		crossDomain: false,
		data: query,
	});
}


function clearMarkers() {
	for(let i=0; i < markers.length; i++) {
		markers[i].setMap(null);
	}
}

function queryLocations() {

	clearMarkers();
	let names =[]
	$('.b-name').each((index, ele) => {
		names.push(ele.textContent);
	});

	let query = {
		'names': names.join(',') 
	};

	
	$.ajax({
		url: '/find_business/locations_query',
		type: 'POST',
		dataType: 'text',
		headers: {
			'X-CSRFToken': csrftoken,
		},
//		 on success, replace new html list
		success: (data) => {
			data=JSON.parse(data)
			console.log(data);
			for (let i =0; i < names.length; i++) {
			markers.push(new google.maps.Marker({
					position: {
						lat: data[i][0],
						lng: data[i][1]
					},
					label: names[i],
					map:map
				}));
			}


		},
//		error: (jqXHR, textStatus,errorThrown ) => {
//			alert('Error: '+errorThrown+'\nStatus:'+jqXHR.status);
//		},
		crossDomain: false,
		data: query,
	});
}


