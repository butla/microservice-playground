import falcon

class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.body = ("\nI've always been more interested in\n"
                     'the future than in the past.\n'
                     '\n'
                     '    ~ Grace Hopper\n\n')

app = falcon.API()
things = ThingsResource()
app.add_route('/', things)
