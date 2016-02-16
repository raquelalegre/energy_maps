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
            print(api.sql('SELECT * FROM energy_tweets'))
        except CartoDBException as e:
            print("Couldn't connect to CartoDB API: ", e)

        return api
