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

    def test_get_all_tweets(self):
        client = CartodbClient()
        tweets = client.get_all_tweets()
        assert len(tweets) > 0

    def test_get_tweets_by_company(self):
        company = 'edfenergy'
        client = CartodbClient()
        tweets = client.get_tweets_by_company(company)
        assert len(tweets) > 0
