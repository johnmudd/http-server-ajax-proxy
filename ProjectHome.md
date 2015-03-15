Tiny HTTP server and proxy.

Written to test GWT apps such as samples/JSON.  By default the JSON sample java reads JSON data from a local file (search-results.js) instead of actually hitting the 3rd party yahoo site.  This server can serve the JSON sample and redirect requests to 3rd party sites such as http://api.search.yahoo.com/.

Based on code from http://effbot.org/librarybook/simplehttpserver.htm