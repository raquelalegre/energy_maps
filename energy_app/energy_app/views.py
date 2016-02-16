from energy_app import app
from flask import render_template
from DataPlotter import DataPlotter

@app.route('/')
def index():
    """
    Displays options to plot data.
    """
    return render_template('index.html')

@app.route('/plot')
def show_plot():
    """
    Displays time series plot containing all tweets.
    """
    plotter = DataPlotter()
    graph = plotter.get_graph()
    return render_template('plot.html', graph=graph)

@app.route('/plot/area/<area>')
def show_plot_by_area(area):
    """
    Displays time series plot containing the tweets of given area.
    """
    plotter = DataPlotter()
    graph = plotter.get_graph(area=area)
    return render_template('plot.html', graph=graph)

@app.route('/plot/company/<company>')
def show_plot_by_company(company):
    """
    Diplays time series plot containing the tweets about given company.
    """
    plotter = DataPlotter()
    graph = plotter.get_graph(company=company)
    return render_template('plot.html', graph=graph)

@app.route('/map')
@app.route('/map/<category>')
def show_map(category=None):
    """
    Displays map with tweets in the requested category.
    """
    return render_template('map.html', category=category)
