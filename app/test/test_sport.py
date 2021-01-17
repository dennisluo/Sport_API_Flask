import unittest
import json

from app import create_app

# Endpoints to test
BASE_URL = 'http://127.0.0.1:5000/'
BPL_URL = 'http://127.0.0.1:5000/sport_api/v1/bpl'
NBA_URL = 'http://127.0.0.1:5000/sport_api/v1/nba'
INVALID_URL = 'http://127.0.0.1:5000/sport_api/v1/tennis'


class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_sport_url_success(self):
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_sport_url_contains_bpl_data(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertIn('bpl_games', data.keys())
        self.assertTrue(data['bpl_games'])

    def test_sport_url_contains_nba_data(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertIn('nba_games', data.keys())
        self.assertTrue(data['nba_games'])

    def test_bpl_url_success(self):
        response = self.app.get(BPL_URL)
        self.assertEqual(response.status_code, 200)

    def test_bpl_url_contains_bpl_data(self):
        response = self.app.get(BPL_URL)
        data = json.loads(response.get_data())
        self.assertTrue(data)

    def test_bpl_url_returns_40_results(self):
        response = self.app.get(BPL_URL)
        data = json.loads(response.get_data())
        keys = len([k for d in data for k in d.keys() if k == 'utcDate'])
        self.assertEqual(keys, 40)

    def test_bpl_url_allows_pagination(self):
        page_query = '?page=1'
        response = self.app.get(BPL_URL + page_query)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data)

    def test_bpl_url_allows_date_query(self):
        date_query = '?date=2021-01-17'
        response = self.app.get(BPL_URL + date_query)
        self.assertEqual(response.status_code, 200)

    def test_bpl_url_invalid_date_returns_empty_list(self):
        date_query = '?date=2099-01-17'
        response = self.app.get(BPL_URL + date_query)
        data = json.loads(response.get_data())
        self.assertEqual(data, [])

    def test_nba_url_success(self):
        response = self.app.get(NBA_URL)
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        response = self.app.get(INVALID_URL)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
