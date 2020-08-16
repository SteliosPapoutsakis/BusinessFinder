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
	
	$('#searchButton').click(() => {
		queryBusiness();
	});
});

	

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
		"lat": (lon)?lon:0.0,
		"lon": (lat)?lat:0.0,
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
		
		},
		error: (jqXHR, textStatus,errorThrown ) => {
			alert('Error: '+errorThrown+'\nStatus:'+jqXHR.status);
		},
		crossDomain: false,
		data: query,
	});
}

