from google.appengine.ext import webapp
import json


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

class GraphJson(webapp.RedirectHandler):
    def post(self):
        pass



app = webapp.WSGIApplication([('/', MainHandler)],
                             debug=True)

