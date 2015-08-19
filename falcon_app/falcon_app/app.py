import falcon
import json
import os
import requests


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


class ChattyResource:

    def __init__(self, external_service_url):
        self.external_service_url = external_service_url

    def on_post(self, req, resp):
        '''
        Adds values 'A' and 'B' from body and multiplies it by the value received from an external service
        '''
        try:
            ext_resp = requests.get(self.external_service_url)
            ext_resp.raise_for_status()
        except requests.HTTPError:
            raise falcon.HTTPServiceUnavailable(
                title='External service unavailable',
                description='Yeah, external service is not responding appropriately.',
                retry_after=1
            )
        multiplier = int(ext_resp.text)

        req_json = json.loads(req.stream.read().decode('utf-8'))
        a, b = int(req_json['A']), int(req_json['B'])
        resp.body = json.dumps((a + b) * multiplier)


# this needs to be set in environment variable
EXTERNAL_ENDPOINT = os.getenv('EXT_SERVICE_URL', '')

app = falcon.API()
app.add_route('/', SampleResource())
app.add_route('/chatty', ChattyResource(EXTERNAL_ENDPOINT))
