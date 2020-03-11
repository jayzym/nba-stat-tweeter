import schedule
import os
import time
import pandas
import twitter
from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

# Variables
last_game_date = ck = cs = atk = ats = ""
FILENAME = os.path.expanduser("~/keys/twitter/keys")

# Functions
def check_and_post(player_name, city):
    """The following function gets the last nuggets game, checks if it's a new game, and posts Nikola Jokic's stats to twitter. Some code snippets were lifted and
    modified from the nba_api and Twitter API Python documentation"""
    global last_game_date
    # Get all teams
    nba_teams = teams.get_teams()

    # Select the dictionary for the selected player's team, which contains their team ID
    player_team = [team for team in nba_teams if team['abbreviation'] == city][0]
    team_id = player_team['id']
    
    # Query for games where the Nuggets were playing
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)

    # The first DataFrame of those returned is what we want.
    games = gamefinder.get_data_frames()[0]
    last_team_game = games.sort_values('GAME_DATE').iloc[-1]
    current_game_date = last_team_game["GAME_DATE"]

    # Get the stats of the game
    game_stats = boxscoretraditionalv2.BoxScoreTraditionalV2(last_team_game["GAME_ID"])

    # Search for player, and build a string of his stats
    for player in game_stats.player_stats.get_dict()["data"]:
        if player_name in player:
            stats = "{0}'s stats for {1} {2}: points: {3}, rebounds: {4}, assists: {5}".format(player_name, last_team_game["GAME_DATE"], last_team_game["MATCHUP"], player[-2], player[-8], player[-7])

    # Make Twitter API
    api = twitter.Api(consumer_key=ck,
        consumer_secret=cs,
        access_token_key=atk,
        access_token_secret=ats)
    try:
        status = api.PostUpdate(stats)
        print("{0} just posted: {1}".format(status.user.name, status.text))
    except UnicodeDecodeError:
        print("Failed to post to Twitter")
        sys.exit(2)



def get_credentials():
    """ The following function loads the keys to authenticate with Twitter"""
    global ck, cs, atk, ats
    lines = open(FILENAME).read().splitlines()
    ck = lines[0]; cs  = lines[1]; atk = lines[2]; ats = lines[3]


print("Enter the player's name:")
player = input()

print("Enter the team the player plays for")
team = input()

get_credentials()
check_and_post(player, team)

"""schedule.every().day.at("10:00").do(check_and_post)
while True:
    schedule.run_pending()
    time.sleep(1)"""
