@echo off
REM start the server
start proxy.py
REM show directory listing
start http://localhost:8080/
REM fetch external site
start http://localhost:8080/__ajaxproxy/http://www.google.com