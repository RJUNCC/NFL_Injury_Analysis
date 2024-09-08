from src.plotly_flask import init_app
import dash
from dash import Input, Output, callback, html, dcc
from src.plotly_flask.dashboard.figures import *

app = init_app()

@dash.callback(
        Output('total_num_injured_graph', 'figure'),
        [Input(component_id='dropdown', component_property="value")]
)
def select_graph(value):
    if value=="Total Number of Injuries":
        return season_total_injuries
    elif value=="Total Games Missed, by all players":
        return season_total_games_missed
    else:
        return season_total_weeks_injured

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083, debug=True, load_dotenv=True)

