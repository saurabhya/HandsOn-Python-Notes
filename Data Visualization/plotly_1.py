"""
    PLotly is a modern platform for plotting and data visualization. Useful for producing a variety of plots,
    espacially for data sciences, Plotly is available for Python, R, JavaScript, Julia and Matlab.
"""

import plotly.graph_objs as go
import plotly as ply
import numpy as np

N = 100
random_x = np.linspace(0,1,N)
random_y0 = np.random.randn(N)+5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)-5

# Crete traces
trace0 = go.scatter(
    x = random_x,
    y = random_y0,
    mode = 'lines',
    name = 'lines'
)
trace1 = go.scatter(
    x = random_x,
    y = random_y1,
    mode = 'lines+markers',
    name = 'lines+markers'
)
trace2 = go.scatter(
    x = random_x,
    y = random_y2,
    mode = 'markers',
    name = 'markers'
)

data = [trace0, trace1, trace2]

ply.offline.plot(data, filename='line-mode')