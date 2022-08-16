import dash
from dash import Dash, html, dcc, Input, Output
# import dash_core_components as dcc
# from dash.dependencies import Input, Output
# import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

app = Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

group_colors = {"control": "light blue", "reference": "red"}

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

df1 = px.data.stocks()


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


def stock_prices():
    # Function for creating line chart showing Google stock prices over time
    fig = go.Figure([go.Scatter(x=df1['date'], y=df1['GOOG'], \
                                line=dict(color='firebrick', width=4), name='Google')
                     ])
    fig.update_layout(title='Server Status',
                      xaxis_title='Dates',
                      yaxis_title='Memory Consumption'
                      )
    return fig


# App Layout
app.layout = html.Div(
    children=[
        # Error Message
        html.Div(id="error-message"),
        # Top Banner
        html.Div(
            className="study-browser-banner row",
            children=[
                html.H2(className="h2-title", children="DISK MANAGEMENT"),
                html.Div(
                    className="div-logo",
                    children=html.Img(
                        className="logo", src=app.get_asset_url("optum_2x.png")
                    ),
                ),
                html.H2(className="h2-title-mobile", children="DISK MANAGEMENT"),
            ],
        ),
        # Body of the App
        html.Div(
            className="row app-body",
            children=[
                # User Controls
                html.Div(
                    className="four columns card",
                    children=[
                        html.Div(
                            className="bg-white user-control",
                            children=[
                                html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("SERVERS"),
                                        dcc.Dropdown(id="study-dropdown",
                                                     options=[
                                                         {'label': 'server1', 'value': 'server1'},
                                                         {'label': 'server2', 'value': 'server1'},
                                                         {'label': 'server3', 'value': 'server1'}
                                                     ],
                                                     value='server1'
                                                     ),

                                    ],
                                ),
                                html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Server Information shown below"),
                                        html.H6("Server Name: APS0007"),
                                        html.H6("App Name: APS0007"),
                                        html.H6("Owner Name: APS0007"),
                                        html.H6("Threshold: APS0007"),
                                        html.H6("Values: APS0007"),

                                        # dcc.RadioItems(
                                        #     id="chart-type",
                                        #     options=[
                                        #         {"label": "Box Plot", "value": "box"},
                                        #         {
                                        #             "label": "Violin Plot",
                                        #             "value": "violin",
                                        #         },
                                        #     ],
                                        #     value="violin",
                                        #     labelStyle={
                                        #         "display": "inline-block",
                                        #         "padding": "12px 12px 12px 0px",
                                        #     },
                                        # ),
                                    ],
                                ),
                                # html.Div(
                                #     className="padding-top-bot",
                                #     children=[
                                #         html.H6("CSV File"),
                                #         dcc.Upload(
                                #             id="upload-data",
                                #             className="upload",
                                #             children=html.Div(
                                #                 children=[
                                #                     html.P("Drag and Drop or "),
                                #                     html.A("Select Files"),
                                #                 ]
                                #             ),
                                #             accept=".csv",
                                #         ),
                                #     ],
                                # ),
                            ],
                        )
                    ],
                ),
                # Graph
                html.Div(
                    className="eight columns card-left",
                    children=[
                        html.Div(
                            className="bg-white",
                            children=[
                                html.H5("Server Prediction"),
                                dcc.Graph(id="plot", figure=stock_prices()),
                            ],
                        )
                    ],
                ),
                dcc.Store(id="error", storage_type="memory"),
                html.Div(className="Card", children=[
                    html.H4(children='Server Param status'),
                    generate_table(df)
                ])
            ],
        ),
    ],

)

if __name__ == "__main__":
    app.run_server(debug=True)
