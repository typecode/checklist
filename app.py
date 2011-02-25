#! /usr/bin/env python

import sys
import os
import datetime
import hashlib

sys.path.append("lib")
import tornado.httpserver
import tornado.httpclient
import tornado.ioloop
import tornado.web

import views.main

import pymongo

print '========================================================================='
print ''
print 'Checklist'
print 'By Andrew Mahon & Type/Code LLC'
print ''
print 'starting..........................'
print ''

print 'Checklist: Loading Configuration Files'
print ''

config_file = open('env.json','r')
try:
  config = tornado.escape.json_decode(config_file.read())
except TypeError, ValueError:
  print 'Checklist: ERROR Loading Configuration Files'
  
if 1 in sys.argv and sys.argv[1] is not None:
  config = config[sys.argv[1]]
else:
  config = config['local']

print 'Checklist: Opening MongoDB Connection'
database = pymongo.Connection('localhost', 27017)
print ''

tornado_settings = {
  "static_path": os.path.join(os.path.dirname(__file__), "ui"),
  "cookie_secret":"This is my tornado secure cookie secret.",
  "login_url": "/login/"
}

application = tornado.web.Application([
  (r"/",views.main.main)
],**tornado_settings)

if __name__ == "__main__":
  print 'Checklist: Starting Tornado HTTPServer'
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(8080)
  tornado.ioloop.IOLoop.instance().start()