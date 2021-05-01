from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models.sources import ColumnDataSource
from bokeh.models.widgets import RangeSlider
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.sampledata.unemployment import data as unemployment
from bokeh.sampledata.us_counties import data as counties
import pandas as pd

df = pd.read_csv('C:/sample_data/tempdata.csv')

source = ColumnDataSource(df)

rs = RangeSlider(start=1940, end=2018, step=5, value=(df.Year.min(), df.Year.max()), title = 'Year')

p = figure(plot_width=800, plot_height=400, title = 'High/Low Temperatures over Time',
       x_axis_label = 'Year', y_axis_label = 'Temperature')
p.scatter(source.data['Year'],source.data['TempHigh'], marker='square', fill_color='red')
p.scatter(source.data['Year'],source.data['TempLow'], marker='square', fill_color='blue')

def update_plot(attr, old, new):
    min_year, max_year = rs.value
    p.x_range.start = min_year
    p.x_range.end = max_year

rs.on_change('value', update_plot)
curdoc().add_root(row(rs, p))
