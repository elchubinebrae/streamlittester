import pandas as pd 
import numpy as np 
import streamlit as st
import math
!pip install lxml
import lxml
# Dictionary with teams categorized by league
leagues_with_urls = {
    'Premier League': {
                     "Arsenal":"https://fbref.com/en/squads/18bb7c10/Arsenal-Stats",
                     "Aston Villa": "https://fbref.com/en/squads/8602292d/Aston-Villa-Stats",
                     "Brentford":"https://fbref.com/en/squads/cd051869/Brentford-Stats",
                     "Brighton": "https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats",
                     "Bournemouth": "https://fbref.com/en/squads/4ba7cbea/Bournemouth-Stats",
                     "Burnley": "https://fbref.com/en/squads/943e8050/Burnley-Stats",
                     "Chelsea": "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats",
                     "Crystal Palace": "https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats",
                     "Everton": "https://fbref.com/en/squads/d3fd31cc/Everton-Stats",
                     "Fulham": "https://fbref.com/en/squads/fd962109/Fulham-Stats",
                     "Liverpool": "https://fbref.com/en/squads/822bd0ba/Liverpool-Stats",
                     "Luton Town": "https://fbref.com/en/squads/e297cd13/Luton-Town-Stats",
                     "Man City": "https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats",
                     "Man Utd": "https://fbref.com/en/squads/19538871/Manchester-United-Stats",
                     "Newcastle United": "https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats",
                     "Nottingham Forest": "https://fbref.com/en/squads/e4a775cb/Nottingham-Forest-Stats",
                     "Sheffield United": "https://fbref.com/en/squads/1df6b87e/Sheffield-United-Stats",
                     "Tottenham Hotspurs": "https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats",
                     "West Ham": "https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats",
                     "Wolverhampton": "https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats",
                     "Napoli": "https://fbref.com/en/squads/d48ad4ff/Napoli-Stats",
                     "Cagliari": "https://fbref.com/en/squads/c4260e09/Cagliari-Stats",
                     "AC Milan": "https://fbref.com/en/squads/dc56fe14/Milan-Stats",
                     "Monza": "https://fbref.com/en/squads/21680aa4/Monza-Stats",
                     "Bayer Leverkusen": "https://fbref.com/en/squads/c7a9f859/Bayer-Leverkusen-Stats",
                     "Eintracht Frankfurt": "https://fbref.com/en/squads/f0ac8ee6/Eintracht-Frankfurt-Stats"
    },
                'Serie A': {
                    "Internationale": "https://fbref.com/en/squads/d609edc0/Internazionale-Stats",
                    "Juventus": "https://fbref.com/en/squads/e0652b02/Juventus-Stats",
                    "Milan": "https://fbref.com/en/squads/dc56fe14/Milan-Stats",
                    "Napoli": "https://fbref.com/en/squads/d48ad4ff/Napoli-Stats",
                    "Roma": "https://fbref.com/en/squads/cf74a709/Roma-Stats",
                    "Bologna": "https://fbref.com/en/squads/1d8099f8/Bologna-Stats",
                    "Fiorentina": "https://fbref.com/en/squads/421387cf/Fiorentina-Stats",
                    "Atalanta": "https://fbref.com/en/squads/922493f3/Atalanta-Stats",
                    "Torino": "https://fbref.com/en/squads/105360fe/Torino-Stats",
                    "Monza": "https://fbref.com/en/squads/21680aa4/Monza-Stats",
                    "Lazio": "https://fbref.com/en/squads/7213da33/Lazio-Stats",
                    "Lecce": "https://fbref.com/en/squads/ffcbe334/Lecce-Stats",
                    "Frosinone": "https://fbref.com/en/squads/6a7ad59d/Frosinone-Stats",
                    "Genoa": "https://fbref.com/en/squads/658bf2de/Genoa-Stats",
                    "Sassuolo": "https://fbref.com/en/squads/e2befd26/Sassuolo-Stats",
                    "Cagliari": "https://fbref.com/en/squads/c4260e09/Cagliari-Stats",
                    "Udinese": "https://fbref.com/en/squads/04eea015/Udinese-Stats",
                    "Empoli": "https://fbref.com/en/squads/a3d88bd8/Empoli-Stats",
                    "Hellas Verona": "https://fbref.com/en/squads/0e72edf2/Hellas-Verona-Stats",
                    "Salernitana": "https://fbref.com/en/squads/c5577084/Salernitana-Stats"
                },
                'Bundesliga': {
                    'Bayer Leverkusen': 'https://fbref.com/en/squads/c7a9f859/Bayer-Leverkusen-Stats',
                    "Bayern Munich": "https://fbref.com/en/squads/054efa67/Bayern-Munich-Stats",
                    "RB Leipzig": "https://fbref.com/en/squads/acbb6a5b/RB-Leipzig-Stats",
                    "Stuttgart": "https://fbref.com/en/squads/598bc722/Stuttgart-Stats",
                    "Dortmund": "https://fbref.com/en/squads/add600ae/Dortmund-Stats",
                    "Hoffenheim": "https://fbref.com/en/squads/033ea6b8/Hoffenheim-Stats",
                    "Frankfurt": "https://fbref.com/en/squads/f0ac8ee6/Eintracht-Frankfurt-Stats",
                    "Freiburg": "https://fbref.com/en/squads/a486e511/Freiburg-Stats",
                    "Wolfsburg": "https://fbref.com/en/squads/4eaa11d7/Wolfsburg-Stats",
                    "Augsburg": "https://fbref.com/en/squads/0cdc4311/Augsburg-Stats",
                    "Munchen": "https://fbref.com/en/squads/32f3ee20/Monchengladbach-Stats",
                    "Heidenheim": "https://fbref.com/en/squads/18d9d2a7/Heidenheim-Stats",
                    "Bochum": "https://fbref.com/en/squads/b42c6323/Bochum-Stats",
                    "Bremen": "https://fbref.com/en/squads/62add3bf/Werder-Bremen-Stats",
                    "Koln": "https://fbref.com/en/squads/bc357bf7/Koln-Stats",
                    "Berlin": "https://fbref.com/en/squads/7a41008f/Union-Berlin-Stats",
                    "Mainz": "https://fbref.com/en/squads/a224b06a/Mainz-05-Stats",
                    "Darmstadt": "https://fbref.com/en/squads/6a6967fc/Darmstadt-98-Stats"

    },
                'La Liga' : {
                    "Real Madrid": "https://fbref.com/en/squads/53a2f082/Real-Madrid-Stats",
                    "Girona": "https://fbref.com/en/squads/9024a00a/Girona-Stats",
                    "CD Alaves": "https://fbref.com/en/squads/8d6fd021/Alaves-Stats",
                    "Barcelona": "https://fbref.com/en/squads/206d90db/Barcelona-Stats",
                    "Athletico Madrid": "https://fbref.com/en/squads/db3b9613/Atletico-Madrid-Stats",
                    "Athletic Club": "https://fbref.com/en/squads/2b390eca/Athletic-Club-Stats",
                    "Real Sociedad": "https://fbref.com/en/squads/e31d1cd9/Real-Sociedad-Stats",
                    "Real Betis": "https://fbref.com/en/squads/fc536746/Real-Betis-Stats",
                    "Getafe": "https://fbref.com/en/squads/7848bd64/Getafe-Stats",
                    "Las Palmas": "https://fbref.com/en/squads/0049d422/Las-Palmas-Stats",
                    "Valencia": "https://fbref.com/en/squads/dcc91a7b/Valencia-Stats",
                    "Rayo Vellecano": "https://fbref.com/en/squads/98e8af82/Rayo-Vallecano-Stats",
                    "Osasuna": "https://fbref.com/en/squads/03c57e2b/Osasuna-Stats",
                    "Alaves": "https://fbref.com/en/squads/8d6fd021/Alaves-Stats",
                    "Villareal": "https://fbref.com/en/squads/2a8183b3/Villarreal-Stats",
                    "Mallorca": "https://fbref.com/en/squads/2aa12281/Mallorca-Stats",
                    "Cadiz": "https://fbref.com/en/squads/ee7c297c/Cadiz-Stats",
                    "Sevilla": "https://fbref.com/en/squads/ad2be733/Sevilla-Stats",
                    "Celta Vigo": "https://fbref.com/en/squads/f25da7fb/Celta-Vigo-Stats",
                    "Grenada": "https://fbref.com/en/squads/a0435291/Granada-Stats",
                    "Almeria": "https://fbref.com/en/squads/78ecf4bb/Almeria-Stats"
                }}

def pick_the_home_team(league, team):
  choice = False
  while choice == False:
    home_choice = team

    try:
      leagues_with_urls[league][home_choice]
      choice = True
    except:
      st.write(f"Did you spell {home_choice} correctly?")

  st.write(f"Thanks for choosing {home_choice}, scraping stats...")
  home_team =  pd.read_html(leagues_with_urls[league][home_choice])
  cleaning_tables_indexes = [0,3,4,5,6,7,8,9,10,11]
  for element in cleaning_tables_indexes:
    home_team_0_columns = home_team[element].columns.get_level_values(1)
    home_team[element].columns = home_team_0_columns
    home_team[element] = home_team[element]
  return home_team

def pick_the_away_team(league, team):
  choice = False
  while choice == False:
    away_choice = team

    try:
      leagues_with_urls[league][away_choice]
      choice = True
    except:
      st.write(f"Did uou spell {away_choice} correctly?")

    st.write(f"Thanks for choosing {away_choice}, scraping stats...")
    away_team =  pd.read_html(leagues_with_urls[league][away_choice])
    cleaning_tables_indexes = [0,3,4,5,6,7,8,9,10,11]
    for element in cleaning_tables_indexes:
      away_team_0_columns = away_team[element].columns.get_level_values(1)
      away_team[element].columns = away_team_0_columns
      away_team[element] = away_team[element]
    return away_team

def get_average_cards_per_game():
  num_home_rows = home_team[11].shape[0]
  num_away_rows = away_team[11].shape[0]
  total_home_cards = home_team[11]["CrdY"][num_home_rows-2] + home_team[11]["CrdR"][num_home_rows-2] + home_team[11]["2CrdY"][num_home_rows-2]
  total_away_cards = away_team[11]["CrdY"][num_away_rows-2] + away_team[11]["CrdR"][num_away_rows-2] + away_team[11]["2CrdY"][num_away_rows-2]
  total_home_games = home_team[11]["90s"][num_home_rows-2]
  total_away_games = away_team[11]["90s"][num_away_rows-2]
  home_average_cards_per_game = total_home_cards/total_home_games
  away_average_cards_per_game = total_away_cards/total_away_games
  average_cards_per_game = home_average_cards_per_game + away_average_cards_per_game
  return math.floor(average_cards_per_game)

def get_average_corners_per_game():
  num_home_rows = home_team[6].shape[0]
  num_away_rows = away_team[6].shape[0]
  corners_home = math.floor(home_team[6]["CK"][home_team[6].shape[0] - 2]/ home_team[6]["90s"][home_team[6].shape[0] - 2])
  away_corners = math.floor(away_team[6]["CK"][away_team[6].shape[0] - 2]/ away_team[6]["90s"][away_team[6].shape[0] - 2])
  return corners_home + away_corners

def find_most_likely_shot_taker(team):
  home_shooters = team[4].drop([team[4].shape[0]-2, team[4].shape[0]-1])
  home_shooters = home_shooters.sort_values(by="90s", ascending=False).reset_index(drop=True).head(7)
  home_shooters = home_shooters.sort_values(by="Sh/90", ascending=False).reset_index(drop=True)
  name= []
  stat = []
  for i in range(0,3):
    name.append(home_shooters.Player[i])
    stat.append(home_shooters["Sh/90"][i])

  for i in range(0,3):
    st.write(f"Highest Shot Taker: {name[i]}, with average of {stat[i]} per match")


def find_shots_on_target(team):
  shooters = team[4].drop([team[4].shape[0]-2, team[4].shape[0]-1])
  #shooters = shooters.sort_values(by="90s", ascending=False).reset_index(drop=True).head(5)

  shooters = shooters.sort_values(by="SoT/90", ascending=False).reset_index(drop=True).head(7)
  name= []
  stat = []
  pos = []
  for i in range(0,6):
    name.append(shooters.Player[i])
    stat.append(shooters["SoT/90"][i])
    pos.append(shooters["Pos"][i])

  for i in range(0,6):
    st.write(f"Most shots on target: {name[i]}, with average of {stat[i]} per match -- Position is {pos[i]}")


def all_player_data_table(league):
  """
  Loops though the teams in the league dictionary and combines
  every player on every team.
  Returns a dataframe that needs to be saved as a
  variable for further use.
  """
  all_player_season_data = pd.DataFrame()
  for club in leagues_with_urls[league].keys():
    all_player_season_data = pd.concat([all_player_season_data,create_team_data_table(pick_the_home_team(league,club))])
  return all_player_season_data

def create_team_data_table(team):
  general_stats = team[0].drop(['xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'PrgR', 'Gls', 'Ast', 'G+A', 'G-PK',
        'G+A-PK', 'xG', 'xAG', 'xG+xAG', 'npxG', 'npxG+xAG', 'Matches','PKatt', ], axis=1)
  general_stats = general_stats.drop([general_stats.shape[0]-2, general_stats.shape[0]-1])
  shooting_stats = team[4].drop(['Nation', 'Pos', 'Age', '90s', 'Gls','G/Sh', 'G/SoT', 'npxG', 'npxG/Sh', 'np:G-xG', 'Matches'], axis=1)
  shooting_stats = shooting_stats.drop([shooting_stats.shape[0]-2, shooting_stats.shape[0]-1])
  passing_stats = team[5].drop(['Nation', 'Pos', 'Age', '90s', 'Att', 'Cmp%',
        'TotDist', 'PrgDist', 'Cmp', 'Att', 'Cmp%', 'Cmp', 'Att', 'Cmp%', 'Cmp',
        'Att', 'Cmp%', 'Ast', 'xAG', 'xA', 'A-xAG', 'KP', '1/3', 'PPA', 'CrsPA',
        'PrgP', 'Matches'], axis=1)
  passing_stats = passing_stats.drop([passing_stats.shape[0]-2, passing_stats.shape[0]-1])
  pass_type_stats = team[6].drop(['Nation', 'Pos', 'Age', '90s', 'Att', 'Live', 'Dead', 'FK',
        'TB', 'Sw', 'Crs','In', 'Out', 'Str', 'Cmp', 'Off',
        'Blocks', 'Matches'],axis=1)
  pass_type_stats = pass_type_stats.drop([pass_type_stats.shape[0]-2, pass_type_stats.shape[0]-1])
  goal_and_shot_creation = team[7].drop(['Nation', 'Pos', 'Age', '90s',
        'PassDead', 'TO', 'Sh', 'Fld', 'Def', 'GCA90', 'PassLive',
        'PassDead', 'TO', 'Sh', 'Fld', 'Def', 'Matches'], axis=1)
  goal_and_shot_creation = goal_and_shot_creation.drop([goal_and_shot_creation.shape[0]-2, goal_and_shot_creation.shape[0]-1])
  defense_columns = list(team[8].columns)
  defense_columns[10] = "DribblersTackled"
  team[8].columns = defense_columns
  defensive_stats = team[8].drop(['Nation', 'Pos', 'Age', '90s','Mid 3rd', 'Att 3rd', 'Tkl', 'Att','Lost',
          'Pass', 'Int', 'Tkl+Int', 'Clr', 'Err', 'Matches'], axis=1)
  defensive_stats = defensive_stats.drop([defensive_stats.shape[0]-2, defensive_stats.shape[0]-1])
  misc_stats = team[11].drop(['Nation', 'Pos', 'Age', '90s', 'CrdY', 'CrdR', '2CrdY','Crs', 'Int', 'TklW', 'PKwon', 'PKcon', 'OG', 'Recov',
        'Won', 'Lost', 'Won%', 'Matches'], axis=1)
  misc_stats = misc_stats.drop([misc_stats.shape[0]-2, misc_stats.shape[0]-1])
  
  frames = [general_stats, shooting_stats, passing_stats, pass_type_stats, goal_and_shot_creation, defensive_stats, misc_stats]

  merged_dfs = frames[0]

  for df in frames[1:]:
      merged_dfs = pd.merge(merged_dfs, df, on="Player", how="left")

  merged_dfs.fillna(0, inplace=True)
  
  return merged_dfs

# Sidebar selectbox for choosing a league
selected_league = st.sidebar.selectbox('Select a league', list(leagues_with_urls.keys()))

# Based on the selected league, populate the teams for that league
selected_teams = leagues_with_urls[selected_league]

# Dropdown for selecting a team from the chosen league
home_name = st.sidebar.selectbox(f'Select Home {selected_league}', selected_teams)
away_name = st.sidebar.selectbox(f'Select Away {selected_league}', selected_teams)
button_go = st.sidebar.button("Lets Do This")

# Display selected teams

if button_go:
    away_team = pick_the_away_team(selected_league, away_name)
    home_team = pick_the_home_team(selected_league, home_name)
    st.write(f"Average Cards Per Game: {get_average_cards_per_game()}")
    st.write(f"Average Total Corners Per Game: {get_average_corners_per_game()}")
    st.write("\n")
    st.write(f"{home_name} Shots Stats --------------------------")
    find_most_likely_shot_taker(home_team)
    st.write(f"{home_name} Shots On Target Stats ----------------")
    find_shots_on_target(home_team)
    st.write("\n")
    st.write(f"{away_name} Stats --------------------------------")
    find_most_likely_shot_taker(away_team)
    st.write(f"{away_name} Shots On Target Stats ----------------")
    find_shots_on_target(away_team)
    st.write("\n")


