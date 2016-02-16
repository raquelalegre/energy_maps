import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def get_time_series(self):
        #Group tweets by time: index by postedtime and resample hourly
        self.data['postedtime'] = pd.to_datetime(self.data['postedtime'])
        timed = self.data.set_index('postedtime')
        hourly = timed.groupby(pd.TimeGrouper('1H'))

        #Elaborate hourly time range covering all tweets
        begin = min(hourly.indices)
        end = max(hourly.indices)
        time_range = pd.date_range(begin, end, freq='H')

        #Index pandas object by time
        print hourly.size().values
        print time_range
        time_series = pd.Series(hourly.size().values, index=time_range)

        return time_series

    def get_histogram(self):
        pass
