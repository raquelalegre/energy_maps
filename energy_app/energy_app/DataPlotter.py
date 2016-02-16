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
        graph = [
            dict(
                data=[
                    dict(
                        x=[1, 2, 3],
                        y=[10, 20, 30],
                        type='scatter'
                    ),
                ],
                layout=dict(
                    title='test graph'
                )
            )
        ]

    def get_data(self):
        data = [
            dict(
                x=[1, 2, 3],
                y=[10, 20, 30],
                type='scatter'
            )
        ]
        return data

    def get_tittle(self):
        return "title"

    def get_layout(self):
        layout = dict(
            title='test graph'
        )
        return layout
