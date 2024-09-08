"""Instantiate a Dash app."""
import dash
from dash import dcc, html, Input, Output, callback
from dash.dash_table import DataTable
from flask import Flask
from pandas import DataFrame
import pandas as pd
import plotly.express as px
from .figures import *

from .data import create_dataframe
from .layout import html_layout


def init_dashboard(app: Flask):
    """
    Create a Plotly Dash dashboard within a running Flask app.

    :param Flask app: Top-level Flask application.
    """
    dash_module = dash.Dash(
        server=app,
        routes_pathname_prefix="/dashapp/",
        external_stylesheets=[
            "../static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    


    # Load DataFrame
    df = create_dataframe()

    # Custom HTML layout
    dash_module.index_string = html_layout

    # Create Layout
    dash_module.layout = html.Div(
        children=[
            dcc.Tabs([
                dcc.Tab(
                    label="Total Injuries by Team", children=[
                        # first graph
                        html.Div(
                            children=[
                                dcc.Graph(
                                    id="total_injuries_for_players_differed_by_played_name",
                                    figure=total_injuries_for_players_differed_by_player_name,
                                ),
                                
                            ],
                        ),
                        # second graph
                        html.Div(
                            children=[
                                
                                dcc.Graph(
                                    id="total_team_injuries",
                                    figure=total_team_injuries
                                ),
                            ],
                            style={
                                        'display':'inline-block', 
                                        'width':'50%', 
                                        'vertical-align':'top',
                                    },
                        ),
                    # create_data_table(df),
                    ]
                ),

                dcc.Tab(
                    label="Seasons",
                    children=[
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id="dropdown",
                                    options=[
                                        {"label":"Total Number of Injuries", "value":"Total Number of Injuries"},
                                        {"label":"Total Number of Injuries", "value":"Total Games Missed, by all players"},
                                        {"label":"Total Number of Injuries", "value":"Total Weeks of Injury, by all players"},
                                    "Total Number of Injuries", 
                                    ],
                                    ),
                                html.Div(dcc.Graph(id="total_num_injured_graph")),
                                html.Div(
                                    html.B(
                                        id="desc-for-seasons-dropdown",
                                        children=[
                                            "The number of injuries, missed games, and missed weeks by all players has decreased from 2012 to 2015."
                                        ],
                                    )
                                )
                            ]
                        )
                    ]
                    )
                
            ])
            
        ],
        
    )
    return dash_module.server


def create_data_table(df: DataFrame) -> DataTable:
    """
    Create Dash DataTable object from Pandas DataFrame.

    :param DataFrame df: Pandas DataFrame from which to build a Dash table.

    :returns: DataTable
    """
    table = DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table