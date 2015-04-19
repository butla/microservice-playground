import falcon


class ThingsResource:
    @staticmethod
    def on_get(req, resp):
        """Handles GET requests"""
        resp.body = 'Hello world\n'
        # print('just logging')

app = falcon.API()
things = ThingsResource()
app.add_route('/', things)
