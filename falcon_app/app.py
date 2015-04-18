import falcon
import sys


class ThingsResource:
    @staticmethod
    def on_get(req, resp):
        """Handles GET requests"""
        resp.body = str(sys.version) + '\n'
        print("----I'm just saying stuff----")

app = falcon.API()
things = ThingsResource()
app.add_route('/', things)
