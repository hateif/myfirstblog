import math

def compute(r):
    return math.sin(r)


import numpy as np
import os
import pandas as pd

def compute_mean_std(filename=None):
    data = np.loadtxt(os.path.join('uploads', filename))
    return """
Data from file <tt>%s</tt>:
<p>
<table border=1>
<tr><td> mean    </td><td> %.3g </td></tr>
<tr><td> st.dev. </td><td> %.3g </td></tr>
""" % (filename, np.mean(data), np.std(data))


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.http import HttpResponse
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.models import Range1d

def computecsvfile(filename=None):
    colnames = ['time', 'value', 'status']
    filename = os.path.join('upload', filename)
    #data_meijiweizhi = pd.read_csv(filename, parse_dates=['time'],header=None,nems=colnames,index_col='time')

    colnames2 = ['t', 'value', 'tt']
    data = pd.read_csv(filename, parse_dates=['time'],header=None,names=colnames,index_col='time')
    #data = pd.read_csv(filename, header=None, names=colnames2, index_col='t')
    data = pd.DataFrame(data)
    #data = np.loadtxt(os.path.join('uploads', filename))
    #data = np.loadtxt(filename)

    x = data.index
    y = data.value




    # select the tools we want
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"


    # build our figures
    p1 = figure(width=800, height=600, x_axis_type="datetime")
    p1.line(x, y, line_width=2, color="red", alpha=0.5)

    # plots can be a single Bokeh Model, a list/tuple, or even a dictionary
    plots = {'Red': p1}

    script, div = components(plots)

    return data.to_html(), script, div

    #return """
        #Data from file <tt>%s</tt>:
            #<p>
                #<table border=1>
                    #<tr><td> mean    </td><td> %.3g </td></tr>
                        #<tr><td> st.dev. </td><td> %.3g </td></tr>
                            #""" % (filename, data.value.mean(), data.value.std())
