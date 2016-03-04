import asyncio
from aiohttp import web


@asyncio.coroutine
def handle(request):
    # schedule something to run in the background
#    asyncio.get_event_loop().create_task(background_stuff())
    
    #name = request.match_info.get('name', "Anonymous")
    text = "Hello world"
    return web.Response(body=text.encode('utf-8'))


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', handle)
    #app.router.add_route('GET', '/{name}', handle)

    srv = yield from loop.create_server(app.make_handler(), '0.0.0.0', 9090)
    print("Server started at http://0.0.0.0:9090")
    return srv


@asyncio.coroutine
def background_stuff():
    yield from asyncio.sleep(5)
    print("5 seconds passed since a call...")


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
