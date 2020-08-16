//
// Front end Javascript for index.html file
// @author Stelios Papoutsakis

let lon,lat;

$(document).ready(() => {

	// set geo location on first click if withint
	$('#within').click(() => {
		if (!lon || !lat) {
			if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition((position) => {
						lon = position.coords.longitude;
						lat = position.coords.latitude;
					});
				} else {
					alert('Geo location is not support by this browser');
				}
		}
	});

	// set toggle for map button
	$('#mapToggle').click(() => {
		if ($('#mapToggle').text() == 'Map') {
			$('#map-row').css('display','block');
			$('.business-list').css('display', 'none');
			$('#mapToggle').text('List');
		} else if ($('#mapToggle').text() == 'List') {
			$('#map-row').css('display','none');
			$('.business-list').css('display', 'block');
			$('#mapToggle').text('Map');
		}
	});
	
	$('#searchButton').click(() => {
		queryBusiness();
	});
});

"use strict";

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: -34.397,
      lng: 150.644
    },
    zoom: 5
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
		},
		error: (jqXHR, textStatus,errorThrown ) => {
			alert('Error: '+errorThrown+'\nStatus:'+jqXHR.status);
		},
		crossDomain: false,
		data: query,
	});
}

