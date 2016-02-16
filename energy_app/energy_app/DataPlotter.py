import json
import plotly
from CartodbClient import CartodbClient
from DataProcessor import DataProcessor

class DataPlotter:
    def __init__(self):
        client = CartodbClient()
        self.data = client.get_all_tweets()
        self.processor = DataProcessor(self.data)

    def get_graph(self):
        #Get the time series data
        time_series = self.processor.get_time_series()

        #Save all the information in a list we can access from the view template
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
