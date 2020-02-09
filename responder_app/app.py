import responder

api = responder.API()


class SampleResource:
    async def on_get(self, req, resp, *, who):
        who = who if who else 'world'
        resp.media = {'hello': who}


if __name__ == '__main__':
    api.add_route('/{who}', SampleResource)
    api.run(port=9090)
