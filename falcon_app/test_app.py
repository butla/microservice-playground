import ddt
import json
from falcon import testing

import app

# TODO: Pokaz trick z importowaniem apki dopiero po ustawieniu sciemnianego kontekstu do testow
# Albo moze jakos inaczej konfiguracje rozwiazac

@ddt.ddt
class SampleTest(testing.TestBase):
    def setUp(self):
        super().setUp()
        self.api = app.app

    def test_sample_get(self):
        self.assertEquals(
            self.simulate_request('/', decode='utf-8'),
            'Hello world\n'
        )

    @ddt.data(
        ({'abra': 123, 'kadabra': 4}, {'abra': 123}),
        ({}, {}),
        ({'nic': 0}, {}),
        ({'abu': 1, 'dabi': 2, 'ABBA': 3}, {'abu': 1, 'ABBA': 3}),
    )
    @ddt.unpack
    def test_sample_post(self, original_dict, expected_dict):
        response = self.simulate_request(
            '/',
            decode='utf-8',
            method='POST',
            body=json.dumps(original_dict),
            headers=[('Content-type', 'application/json')]
        )

        self.assertEquals(
            response,
            json.dumps(expected_dict)
        )
