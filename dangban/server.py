#! encoding:utf-8

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('',8888,application)
print "Server HTTP on port 8888..."
httpd.serve_forever()
