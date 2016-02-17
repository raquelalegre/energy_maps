from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class GraphForm(Form):
    company = StringField('company',)
    map_types = ['', 'Heatmap', 'AnimationByCategory', 'AnimationCummulative', 'Interactive']
    map_type = SelectField('map_type', choices = [(m, m) for m in map_types])
    areas = ['', 'Global', 'uk_administrative_regions']
    area = SelectField('area', choices = [(a, a) for a in areas])
