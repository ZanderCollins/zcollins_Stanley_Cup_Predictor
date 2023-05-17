# File created by Zander Collins 

# imports library requests
import requests
from bs4 import BeautifulSoup 
import pandas as pd

# pulls player stats from websites
url = 'https://www.hockey-reference.com/leagues/NHL_2023_skaters.html'
response = requests.get(url)

# adds in html parser which assists with webscraping
soup = BeautifulSoup(response.text, 'html.parser')


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
    print(Name[i].text + " " + Goals[i].text + " Goals " + Assists[i].text + " Assists " 
          + PenaltyMinutes[i].text + " Penalty Minutes ") 
    
    Goal_Points = int(Goals[i].text) * 2 
    Assist_Points = int(Assists[i].text)
    Penalty_Points = int(PenaltyMinutes[i].text) * -.15
    TotalPoints = Goal_Points + Assist_Points + Penalty_Points
    TotalPointsIndex = "players ranked highest to lowest based on number of Total Points"

    print("Total Points: " + str(TotalPoints))

