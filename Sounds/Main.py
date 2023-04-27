# File created by Zander Collins 

''' 
Goal:

Scrape data off NHL stats website 
retrieve data/stats of each play off team
compare data/stats for each round in the playoffs
give a final winner or prediction 

Website = https://bracketchallenge.nhl.com/en/bracket?bracket_id=1&entry_id=611085"

'''

'''
brainstorming:
get matchups off of website 
base chance = 50/50 
asses 3 different variables off website
    -goals per game
    -goals against
    -power place percentage
for the team with greater stat
    -take away 3% from the other team 
    -add 3% to team win percentage 
run all 3 comparisons
get final win percentages = x% vs y%
randomly choose between given the percentages
winner of round is established 
create second round 
redo given comparion again 
until the final winner is chosen
''' 