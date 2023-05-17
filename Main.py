# File created by Zander Collins 
# Minor help recieved from my dad(very smart computer guy(masters in Computer Science))

# imports library requests
import requests
from bs4 import BeautifulSoup 
import pandas as pd

# pulls player stats from websites
url = 'https://www.hockey-reference.com/leagues/NHL_2023_skaters.html'
response = requests.get(url)

# adds in html parser which assists with webscraping
soup = BeautifulSoup(response.text, 'html.parser')

player_stats = []

# defines the name of each player
Name = soup.findAll("td", attrs={"data-stat":"player"})
# defines the goals scored by each player this season so far 
Goals = soup.findAll("td", attrs={"data-stat":"goals"})
# defines the primary assists of each player this season so far
Assists = soup.findAll("td", attrs={"data-stat":"assists"})
# defines the team's power play percentage from the website 
PenaltyMinutes = soup.findAll("td", attrs={"data-stat":"pen_min"})

# a loop that will print the stats of the categories from the website
for i in range(len(Name)):
    # assigns the specific web information/stats into usable variables 
    player_name = Name[i].text
    goals = int(Goals[i].text)
    assists = int(Assists[i].text)
    penalty_minutes = int(PenaltyMinutes[i].text)

    # translates the raw player stats into the fantasy/point amounts
    Goal_Points = goals * 2 
    Assist_Points = assists
    Penalty_Points = penalty_minutes * -.15
    Total_Points = Goal_Points + Assist_Points + Penalty_Points

    # creates a list to hold all of the stats/information of a given player 
    player_stats.append({
        'Player' : player_name, 
        'Goals' : goals, 
        'Assists' : assists, 
        'Penalty Minutes' : penalty_minutes, 
        'Total Points' : Total_Points
    })

# function that sorts the players from least to most total points -> worst = 1, best = max
sorted_player_stats = sorted(player_stats, key=lambda x: x['Total Points'])

# ranks the players from worst to best and displays their name and all of the parts that make up player_stats 
for rank, player in enumerate(sorted_player_stats, start = 1):
    print(f"Rank {len(sorted_player_stats) - rank + 1}: {player['Player']}")
    print(f"Goals: {player['Goals']}")
    print(f"Assists: {player['Assists']}")
    print(f"Penalty Minutes: {player['Penalty Minutes']}")
    print(f"Total Points: {player['Total Points']}")
    print()
