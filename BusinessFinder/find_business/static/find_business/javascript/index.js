//
// Front end Javascript for index.html file
// @author Stelios Papoutsakis
//
$(document).ready(() => {
	console.log('hello');
	queryBusiness('');
});




/**
 * Querys the backend for matching business
 *
 * @input (json), paramters for query
 * @output (list), list of matching json objects
 */

function queryBusiness(queryParams) {
	let test = {
		"type": "resturant",
		"Title": "Mario's Pizza",
		"Address": "8 Lane 7897",
	};
	
	$.ajax({
		url: '/find_business/business_query',
		type: 'POST',
		dataType: 'json',
		headers: {
			'X-CSRFToken': csrftoken,
		},
		crossDomain: false,
		data: test,
	}).then((response => { console.log('ji'); }));
}

/**
 * updates the client side based on a new list of business
 *
 * @input (json), list of new business
 */

function updateBusinessList(listOfBusiness) {
	console.log(listOfBusiness);
}

