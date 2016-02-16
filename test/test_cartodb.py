import pytest
from CartodbClient import CartodbClient, CartoDBException

class TestCartoDB:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_cartodb_connection(self):
        try:
            client = CartodbClient()
        except CartoDBException:
            pytest.fail("Couldn't connect to CartoDB")

    def test_get_tweets(self):
        client = CartodbClient()
        api = client.api
        tweets = api.sql('SELECT * FROM energy_tweets_table')
        assert len(tweets) > 0
