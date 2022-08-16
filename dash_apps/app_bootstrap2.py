"""
A simple app demonstrating how to dynamically render tab content containing
dcc.Graph components to ensure graphs get sized correctly. We also show how
dcc.Store can be used to cache the results of an expensive graph generation
process so that switching tabs is fast.
"""
import time

import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html

from dash_apps.dash_bootstrap_version import nav_item, dropdown, PLOTLY_LOGO

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# app.layout = dbc.Container(
#     [
#         dcc.Store(id="store"),
#         html.H1("Dynamically rendered tab content"),
#         html.Hr(),
#         dbc.Button(
#             "Regenerate graphs",
#             color="primary",
#             id="button",
#             className="mb-3",
#         ),
#         dbc.Tabs(
#             [
#                 dbc.Tab(label="Scatter", tab_id="scatter"),
#                 dbc.Tab(label="Histograms", tab_id="histogram"),
#             ],
#             id="tabs",
#             active_tab="scatter",
#         ),
#         html.Div(id="tab-content", className="p-4"),
#     ]
# )

logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Logo", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://optum.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [nav_item, dropdown],
                    className="ms-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ],
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

app.layout = dbc.Container(
    [   logo,
        dbc.Row(
            [
                dbc.Col(html.H1('Test1'), width=12),
                dbc.Col(html.H1('Test2'), width=12)
            ]
        )
    ]
)

# @app.callback(
#     Output("tab-content", "children"),
#     [Input("tabs", "active_tab"), Input("store", "data")],
# )
# def render_tab_content(active_tab, data):
#     """
#     This callback takes the 'active_tab' property as input, as well as the
#     stored graphs, and renders the tab content depending on what the value of
#     'active_tab' is.
#     """
#     if active_tab and data is not None:
#         if active_tab == "scatter":
#             return dcc.Graph(figure=data["scatter"])
#         elif active_tab == "histogram":
#             return dbc.Row(
#                 [
#                     dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
#                     dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
#                 ]
#             )
#     return "No tab selected"
#
#
# @app.callback(Output("store", "data"), [Input("button", "n_clicks")])
# def generate_graphs(n):
#     """
#     This callback generates three simple graphs from random data.
#     """
#     if not n:
#         # generate empty graphs when app loads
#         return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}
#
#     # simulate expensive graph generation process
#     time.sleep(2)
#
#     # generate 100 multivariate normal samples
#     data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)
#
#     scatter = go.Figure(
#         data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
#     )
#     hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
#     hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])
#
#     # save figures in a dictionary for sending to the dcc.Store
#     return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2}


if __name__ == "__main__":
    app.run_server(debug=True, port=8060)