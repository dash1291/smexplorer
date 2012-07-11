$( document ).ready( function() {
	var dirPath = $( '#dir-path' ).val();
	var sitePrefix = $( '#site-prefix' ).val();
	var remotePrefix = $( '#remote-prefix' ).val();
	$( '#breadcrumb' ).BreadCrumb( dirPath, sitePrefix + '/dir' );
	
	var searchTimeout = null;
	$( '#search-text' ).keyup( function() {
		var text = this.value;
		if( searchTimeout ) {
			clearTimeout( searchTimeout );
		}
		searchTimeout = setTimeout( function () {
			var searchUri = sitePrefix + '/search/' + text;
			console.log(searchUri);
			$.get( searchUri, function( data ) {
				$( '#search-overlay' ).html( '' );
				for( i in data.directories ) {
					var name = data.directories[ i ].name;
					var path = data.directories[ i ].path;
					element = '<div class="dir-search-item directory-item">' +
						'<a class="dir-link" href="' + sitePrefix + '/dir/' + path + '">' +
							name + '/' + '</a>' +
						'</div>';
					$( '#search-overlay' ).append( element );
				}

				for( i in data.files ) {
					var name = data.files[ i ].name;
					var path = data.files[ i ].path;
					element = '<div class="file-search-item file-item">' +
						'<a class="file-link" href="' + remotePrefix + path + '/' + name + '">' +
							name + '</a>' +
						'</div>';
					$( '#search-overlay' ).append( element );
				}
				$( '#search-overlay' ).show();
			});
			// search now
			searchTimeout = false;
		}, 500 );
	});
});
