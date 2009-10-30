#! /usr/bin/env python

'''
AJAX proxy

Serve HTTP pages.  Allow an AJAX script to access a 3rd party site.


Example using the GWT JSON sample application.

1) Modify JSON source code.
	$ cd gwt-linux-1.4.62/samples/JSON/src/com/google/gwt/sample/json/client
	Edit JSON.java

	Change this line:
	    private static final String DEFAULT_SEARCH_URL = "search-results.js";
	to this:
		private static final String DEFAULT_SEARCH_URL = "http://localhost:8080/__ajaxproxy/http://api.search.yahoo.com/ImageSearchService/V1/imageSearch?appid=YahooDemo&query=potato&results=2&output=json";

2) Compile the JSON code as usual.
	$ cd gwt-linux-1.4.62/samples/JSON
	$ JSON-compile

3) Start this server.
	$ cd gwt-linux-1.4.62/samples/JSON/www/com.google.gwt.sample.json.JSON
	$ proxy.py .  # Serve files from current directory.

3) Access the app in your browser using this URL.
	http://localhost:8080/JSON.html

4) Presss the Search button to access JSON data from yahoo site.


Based on code from http://effbot.org/librarybook/simplehttpserver.htm

'''

import urllib.request
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

PORT = 8080

def get_next_free_port(port):
	s = socket.socket()
	try:
		s.connect(('localhost', port))
		return get_next_free_port(port + 1)
	except socket.error:
		return port

class myHTTPServer(SimpleHTTPRequestHandler):
	def do_GET(self):
		# Is this a special request to /__ajaxproxy/
		prefix = '/__ajaxproxy/'
		if self.path.startswith(prefix):
			# Strip off the prefix.
			newPath = self.path.lstrip(prefix)
			print ('GET remote: ', newPath)
			try:
				self.copyfile(urllib.request.urlopen(newPath), self.wfile)
			except IOError as e:
				print ("ERROR:   ", e)
		else:
			SimpleHTTPRequestHandler.do_GET(self)
		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	pass

def main():
	try:	
		next_free_port = get_next_free_port(PORT)
		server = ThreadedHTTPServer(('',next_free_port),myHTTPServer)
		print ('server started at port ', next_free_port)
		server.serve_forever()
	except KeyboardInterrupt:
		server.socket.close()

if __name__=='__main__':
    main()