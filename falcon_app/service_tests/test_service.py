import os
import requests
import subprocess
import time
import socket

class TestService:
    @classmethod
    def setup_class(cls):
        # try:
        cls._app_process = cls._start_app()
        cls._mb_process = cls._start_mountebank()

        cls._wait_for_endpoint('localhost:9090')
        cls._wait_for_endpoint('localhost:2525')

        TestService._configure_mountebank()
        # except:
        #     cls.teardown_class()
        #     raise

    @classmethod
    def teardown_class(cls):
        cls._stop_mountebank()
        cls._app_process.kill()

    @classmethod
    def _start_mountebank(cls):
        mb_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../tools/mountebank-v1.2.122-linux-x64/mb')
        mb_proc = subprocess.Popen(mb_path)
        return mb_proc

    @classmethod
    def _stop_mountebank(cls):
        mb_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../tools/mountebank-v1.2.122-linux-x64/mb')
        subprocess.call([mb_path, 'stop'])

    @staticmethod
    def _wait_for_endpoint(address, timeout=5.0):
        host, port_str = address.split(':')
        port = int(port_str)
        start_time = time.perf_counter()
        while True:
            try:
                with socket.create_connection((host, port)):
                    pass
            except ConnectionRefusedError:
                if time.perf_counter() - start_time >= timeout:
                    raise TimeoutError("Endpoint {} didn't appear in time.".format(address))

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
        return app_proc

    @staticmethod
    def _set_app_environment():
        os.environ['EXT_SERVICE_URL'] = 'http://localhost:4545'

    def test_service_chatty_endpoint(self):
        returned_value = requests.post('http://localhost:9090/chatty', json={'A': 1, 'B': 4}).json()
        assert returned_value == 15
