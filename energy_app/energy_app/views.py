from energy_app import app
from flask import render_template, redirect, url_for, request, flash
from DataPlotter import DataPlotter
from Forms import GraphForm

app.config.from_object('config')

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Displays options to plot data.
    """
    form = GraphForm()
    if form.validate_on_submit():
        company = form.company.data
        area = form.area.data
        map_type = form.map_type.data
        if company != '':
            return redirect(url_for('show_plot_by_company', company=company))
        if area != '':
            return redirect(url_for('show_plot_by_area', area=area))
        if map_type != '':
            return redirect(url_for('show_map', category=map_type))
    return render_template('index.html', form=form)

@app.route('/plot/area/<area>')
def show_plot_by_area(area):
    """
    Displays time series plot containing the tweets of given area.
    """
    plotter = DataPlotter()
    if area.lower() == "global":
        graph = plotter.get_graph()
    else:
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
