import pandas as pd
import plotly.express as px

nfl_teams = pd.read_csv("data/NFL Teams.csv")
total_team_injuries = px.histogram(
    data_frame=nfl_teams,
    y="Team",
    x="Total Number of Injuries (2012-2014)",
    template="ggplot2"
)

head_injuries = pd.read_csv("data/Head Injured Players.csv")
total_injuries_for_players_differed_by_player_name = px.bar(
    data_frame=head_injuries.groupby(by="Player")["Total Number of Injuries (2012-2014)"].sum().reset_index(),
    x="Player",
    y="Total Number of Injuries (2012-2014)",
    template="ggplot2",
)

seasons = pd.read_csv("data/Seasons.csv")

season_total_injuries = px.histogram(
    data_frame=seasons,
    x="Season",
    y="Total Number of Injuries",
    template="ggplot2",
    title="Total Number of Injuries vs Seasons"
)

season_total_games_missed = px.histogram(
    data_frame=seasons,
    x="Season",
    y="Total Games Missed, by all players",
    template="ggplot2",
    title="Total Games Missed of all players vs Seasons"
)

season_total_weeks_injured = px.histogram(
    data_frame=seasons,
    x="Season",
    y="Total Weeks of Injury, all its players",
    template="ggplot2",
    title="Total Weeks of Injury of all players vs Seasons"
)
