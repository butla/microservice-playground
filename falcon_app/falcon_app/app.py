import falcon
import json

class SampleResource:
    @staticmethod
    def on_get(req, resp):
        resp.body = 'Hello world\n'

    @staticmethod
    def on_post(req, resp):
        '''
        Given JSON input returns a JSON with only the keys that start with "A" (case insensitive).
        '''
        if req.content_type != 'application/json':
            raise falcon.HTTPUnsupportedMediaType('Media type needs to be application/json')
        body_json = json.loads(req.stream.read().decode('utf-8'))
        resp.body = json.dumps({key: value for key, value in body_json.items() if key.lower().startswith('a')})


app = falcon.API()
app.add_route('/', SampleResource())
