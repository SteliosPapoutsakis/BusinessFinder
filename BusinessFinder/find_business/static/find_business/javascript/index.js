//
// Front end Javascript for index.html file
// @author Stelios Papoutsakis


$(document).ready(() => {
	$('#within').click(() => {
		if (!lat || !lon) {
			if (navigator.geolocation) {
				navigator.geolocation.getCurrentPosition((position) => {

				);
			} else {
				alert('Geo location is not support by this browser');
			}
		});
	queryBusiness('');
});


function geQueryParams() {
	params = {
		"type": $('#type').text()
	}

	return params;
		


/**
 * Querys the backend for matching business
 *
 * @input (json), paramters for query
 * @output (list), list of matching json objects
 */
function queryBusiness(queryParams) {
	let test = {
		"type": "resturant",
		"title": "Mario's Pizza",
		"lat": 0.0,
		"lon": 0.0,
		"within": 3
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

/**
 *
