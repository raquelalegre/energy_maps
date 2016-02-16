import json
import plotly
from CartodbClient import CartodbClient
from DataProcessor import DataProcessor

class DataPlotter:
    """
    Formats data to be plotted by Plotly.
    """
    def __init__(self):
        self.client = CartodbClient()

    def get_graph(self, area=None, company=None):
        """
        Queries tweets by given area/company filter.
        """
        # Get all tweets or filtered by area
        if area:
            data = self.client.get_tweets_by_area(area)
        elif company:
            data = self.client.get_tweets_by_company(company)
        else:
            data = self.client.get_all_tweets()

        processor = DataProcessor(data)

        # Get the time series data
        time_series = processor.prepare_time_series()

        # Save all the graph info in a list we can access from the view template
        graph = [
            dict(
                data=[
                    dict(
                        x=time_series.index,
                        y=time_series
                    )
                ],
                layout=dict(
                    title='Tweet Frequency'
                ),
                id = 'timeseries'
            )
        ]

        # Plotly needs the graph/pandas data encoded in compatible JSON format
        graph = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

        return graph
