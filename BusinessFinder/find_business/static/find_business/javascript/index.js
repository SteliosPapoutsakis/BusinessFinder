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
						alert(lon +' '+lat);
					});
				} else {
					alert('Geo location is not support by this browser');
				}
		}
	});

	queryBusiness();
});


	

/**
 * Querys the backend for matching business
 *
 * @input (json), paramters for query
 * @output (list), list of matching json objects
 */
function queryBusiness() {
 	let type = 	$('#type').val();
	let search = $('#search').val();
	console.log(type+' '+search);
	let test = {
		"type": "resturant",
		"search": "Mario's Pizza",
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
		data: test,
	});
}

