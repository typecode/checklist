import sys


sys.path.append("lib")
import tornado.httpclient
import json
import pymongo
import pymongo.json_util

class main(tornado.web.RequestHandler):
  
  def initialize(self,connections={}):
    print '-views.main.main.initialize'
  
  def get(self):
    print '-views.main.main.get'
    self.render("../ui/index.html", title="My title")
    
  def get_current_user(self):
    print '-views.main.main.get_current_user'
    return None

    