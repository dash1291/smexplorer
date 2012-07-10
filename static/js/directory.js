$( document ).ready( function() {
	var dirPath = $( '#dir-path' ).val();
	var sitePrefix = $( '#site-prefix' ).val();
	$( '#breadcrumb' ).BreadCrumb( dirPath, sitePrefix );
});
