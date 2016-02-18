import pandas as pd
import numpy as np

class DataProcessor:
    """
    Class in charge of data manipulation, cleaning and preparation to plot.
    """
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def prepare_time_series(self):
        """
        Elaborate data to get the number of tweets per hourly interval.
        """
        #Group tweets by time: index by postedtime and resample hourly
        self.data['postedtime'] = pd.to_datetime(self.data['postedtime'])
        timed = self.data.set_index('postedtime')
        hourly = timed.groupby(pd.TimeGrouper('1H'))

        #Elaborate hourly time range covering all tweets
        begin = min(hourly.indices)
        end = max(hourly.indices)
        time_range = pd.date_range(begin, end, freq='H')

        #Index pandas object by time
        time_series = pd.Series(hourly.size().values, index=time_range)

        return time_series

    def clean_data(self):
        pass
