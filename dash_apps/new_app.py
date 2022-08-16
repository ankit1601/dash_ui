# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application disk management and self healing of server.
    '''),
    html.Label('Server Details'),
    dcc.Dropdown(['APP_Server3', 'APP_Server1', 'APP_Server2'], 'APP_Server1'),

    html.Div(children=[
        html.Div(children=[html.H1("Server Details"),
                           html.H4("Name"),
                           html.H4("Threshold"),
                           html.H4("Health")], style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'width': '49%', 'display': 'inline-block'}
    )])


])

if __name__ == '__main__':
    app.run_server(debug=True)
