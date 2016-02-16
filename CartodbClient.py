import json
from cartodb import CartoDBAPIKey, CartoDBException

class CartodbClient:
    def __init__(self):
        self.api = self.get_api()

    def get_api(self):
        """
        Reads secrets from local file and connects to CartoDB API.
        """
        with open('secrets.json') as secrets_file:
            secrets = json.load(secrets_file)

        api_key = secrets['api_key']
        cartodb_domain = secrets['cartodb_domain']

        api = CartoDBAPIKey(api_key, cartodb_domain)

        try:
            api.sql('SELECT * FROM energy_tweets_table')
        except CartoDBException:
            raise

        return api

    def get_tweets(self):
        """
        Connect to CartoDB and get list of energy tweets.
        """
        tweets = self.api.sql('SELECT * FROM energy_tweets_table')
        return tweets

    def get_tweets(self, where):
        sql_query = """
            SELECT actor_preferredusername, body, postedtime,
            the_geom_webmercator
            FROM energy_tweets_table
            {0}""".format(where)
        results = self.api.sql(sql_query)
        #tweets info is contained in the rows field of the returned json results
        tweets = results['rows']
        return tweets

    def get_all_tweets(self):
        tweets = self.get_tweets('')
        return tweets

    def get_tweets_by_company(self, company):
        sql_where = "WHERE body LIKE '%{0}%'".format(company)
        tweets = self.get_tweets(sql_where)
        return tweets
