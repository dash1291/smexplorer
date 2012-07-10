/**
 * Generate breadcrumb navigation for a basic given path and a URL prefix,
 * with this jQuery plugin.
 *
 * Usage $(#element).BreadCrumb( path, prefix )
 * example, path = root/level1/level2/level2
 * prefix = http://exampleurl.com
 *
 * @author Ashish Dubey(ashish.dubey91@gmail.com)
**/

(function( $ ) {
	$.fn.BreadCrumb = function( path, prefix ) {
		var dirTokens = path.split('/');
		var traversed = '';
		for( i in dirTokens ) {
			var element = '<a href="' + prefix + '/' + traversed + dirTokens[i] +
										'">' + dirTokens[i] + '</a> > '
			traversed = traversed + dirTokens[i] + '/';
			console.log(element);
			$( this ).append( element );
		}
	};
} )( jQuery );
