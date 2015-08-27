import os
import requests
import subprocess
import time
import socket
import logging

from urllib.parse import urlparse

class TestService:
    @classmethod
    def setup_class(cls):
        cls._app_process = cls._start_app()
        cls._mb_process = cls._start_mountebank()

        TestService._configure_mountebank()

    @classmethod
    def teardown_class(cls):
        cls._stop_mountebank()
        cls._app_process.kill()

    @classmethod
    def _start_mountebank(cls):
        mb_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../tools/mountebank-v1.2.122-linux-x64/mb')
        # TODO this should wait for the endpoint to get up
        mb_proc = subprocess.Popen(mb_path)
        try:
            TestService._wait_for_endpoint('http://localhost:2525/imposters')
        except Exception:
            logging.exception("Mountebank didn't start")
            TestService._stop_mountebank()
            raise

        return mb_proc

    @staticmethod
    def _stop_mountebank():
        mb_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../tools/mountebank-v1.2.122-linux-x64/mb')
        subprocess.check_call([mb_path, 'stop'])

    @staticmethod
    def _wait_for_endpoint(url, timeout=5.0):
        """
        Waits for the HTTP endpoint to appear by trying to connect to it with TCP.
        :param str url: Service url, e.g. "http://localhost:2525/imposters". Port needs to be specified.
        :rtype: None
        """
        parserd_url = urlparse(url)
        host, port_str = parserd_url.netloc.split(':')
        port = int(port_str)

        start_time = time.perf_counter()
        while True:
            try:
                with socket.create_connection((host, port)):
                    break
            except ConnectionRefusedError:
                time.sleep(0.001)
                if time.perf_counter() - start_time >= timeout:
                    raise TimeoutError('Waited too long fot the process')

    @staticmethod
    def _configure_mountebank():
        resp = requests.post('http://localhost:2525/imposters', json={
            "port": 4545,
            "protocol": "http",
            "stubs": [
                {
                    "responses": [
                        {
                            "is": {
                                "statusCode": 200,
                                "headers": {
                                    "Content-Type": "application/json"
                                },
                                "body": "3"
                            }
                        }
                    ],
                    "predicates": [
                        {
                            "and": [
                                {
                                    "equals": {
                                        "path": "/",
                                        "method": "GET",
                                    }
                                },
                            ]
                        }]
                }]
        })
        resp.raise_for_status()

    @classmethod
    def _start_app(cls):
        TestService._set_app_environment()

        project_root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
        os.chdir(project_root_path)
        app_proc = subprocess.Popen(['gunicorn', 'falcon_app.app:app', '--bind', ':9090'])

        try:
            TestService._wait_for_endpoint('http://localhost:9090')
        except Exception:
            logging.exception("App didn't start")
            app_proc.kill()
            raise

        return app_proc

    @staticmethod
    def _set_app_environment():
        os.environ['EXT_SERVICE_URL'] = 'http://localhost:4545'

    def test_service_chatty_endpoint(self):
        returned_value = requests.post('http://localhost:9090/chatty', json={'A': 1, 'B': 4}).json()
        assert returned_value == 15
