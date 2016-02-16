import pytest
from cartodb import CartoDBException
from ..CartodbClient import CartodbClient

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
        assert len(tweets) == 8813

    def test_get_tweets_by_company(self):
        company = 'edfenergy'
        client = CartodbClient()
        tweets = client.get_tweets_by_company(company)
        assert len(tweets) == 1325

    def test_get_tweets_by_area(self):
        area = 'uk_administrative_regions'
        client = CartodbClient()
        tweets = client.get_tweets_by_area(area)
        assert len(tweets) == 7236
