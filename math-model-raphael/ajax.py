__author__ = 'chexov'


from google.appengine.ext import webapp
import json
from math.mnk import *

class AjaxPoint(webapp.RequestHandler):
    def post(self):
        print self.request