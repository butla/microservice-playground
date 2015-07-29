import ddt
import json
from falcon import testing

from falcon_app.app import app


@ddt.ddt
class SampleTest(testing.TestBase):
    BENCHMARK_WORDS = {
        'malpighiaceous': 'nonexternality',
        'OVERCENSURIOUS': 'pantomimicry',
        'artigas': 'bijouterie',
        'AFRIKAANS': 'overwearying',
        'argones': 'knickered',
        'CENTRODOSAL': 'contentness',
        'untremulant': 'unintrenchable',
        'VIPERISHLY': 'remasticated',
        'clear': 'piece',
        'BURRIED': 'gritty',
        'awesome': 'stiff',
        'RUM': 'soul',
        'rct': 'polis',
        'AFGHANISTAN': 'yodelled',
        'PRELUDIOUSLY': 'exemplarity',
        'schrik': 'ekaterinburg',
        'albania': 'gynephobia',
        'SHORTCUT': 'subtiliser',
        'super': 'gaillardia',
        'INEPTLY': 'hoper',
        'ANDORRA': 'hodgepodge',
    }

    BENCHMARK_WORDS_FILTERED = {
        'artigas': 'bijouterie',
        'AFRIKAANS': 'overwearying',
        'argones': 'knickered',
        'awesome': 'stiff',
        'AFGHANISTAN': 'yodelled',
        'albania': 'gynephobia',
        'ANDORRA': 'hodgepodge',
    }

    def setUp(self):
        super().setUp()
        self.api = app

    def test_sample_get(self):
        self.assertEqual(
            self.simulate_request('/', decode='utf-8'),
            'Hello world\n'
        )

    @ddt.data(
        ({'abra': 123, 'kadabra': 4}, {'abra': 123}),
        ({}, {}),
        ({'nic': 0}, {}),
        ({'abu': 1, 'dabi': 2, 'ABBA': 3}, {'abu': 1, 'ABBA': 3}),
        (BENCHMARK_WORDS, BENCHMARK_WORDS_FILTERED),
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

        self.assertEqual(
            json.loads(response),
            expected_dict
        )
