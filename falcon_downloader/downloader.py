import concurrent.futures
import falcon
import time
import urllib.request
import json

from urllib.parse import urlsplit


class DownloaderResource:
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=20)

    @staticmethod
    def on_post(req, resp):
        body = json.loads(req.stream.read().decode('utf-8'))
        future = DownloaderResource.pool.submit(DownloaderResource.download_file, body['url'])
        future.add_done_callback(lambda future, start_time=time.perf_counter():
                                 print('Downloaded in', time.perf_counter() - start_time, 'seconds'))
        resp.body = 'Download scheduled.\n'

    @staticmethod
    def download_file(file_url):
        path = urlsplit(file_url).path
        file_name = path.split('/')[-1]

        chunk_size = 16 * 1024
        with urllib.request.urlopen(file_url) as resp:
            with open(file_name, 'wb') as f:
                while f.write(resp.read(chunk_size)):
                    pass


app = falcon.API()
app.add_route('/', DownloaderResource())