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

    def get_tweets(self, where):
        sql_query = """
            SELECT actor_preferredusername, body, postedtime, category_terms,
            the_geom_webmercator
            FROM energy_tweets_table
            {0}""".format(where)
        results = self.api.sql(sql_query)
        #tweets info is contained in the rows field of the returned json results
        tweets = results['rows']
        return tweets

    def get_all_tweets(self):
        sql_where = ''
        tweets = self.get_tweets(sql_where)
        return tweets

    def get_tweets_by_company(self, company):
        sql_where = "WHERE category_terms LIKE '%{0}%'".format(company)
        tweets = self.get_tweets(sql_where)
        return tweets

    def get_tweets_by_area(self, area):
        #Use postgres to filter by area
        sql_query = """
        SELECT * FROM
            (SELECT * FROM energy_tweets_table) AS et,
            (SELECT the_geom_webmercator AS gwm
                FROM {0}) AS shp
        WHERE ST_WITHIN(et.the_geom_webmercator, shp.gwm)""".format(area)
        results = self.api.sql(sql_query)
        return results['rows']
