# Made by Zander Collins
# Help from https://www.zenrows.com/blog/speed-up-web-scraping-with-concurrency-in-python#concurrency
# Web scapper setup 

import requests
from bs4 import BeautifulSoup 
import csv 

base_url = "https://bracketchallenge.nhl.com/en/bracket?bracket_id=1&entry_id=611085"
page = requests.get(base_url)
pages = range(1)

def extract_details(page): 
	# concatenate page number to base URL 
	response = requests.get(f"{base_url}/{page}/") 
	soup = BeautifulSoup(response.text, "html.parser") 
 
	Teams_list = [] 
	for teams in soup.select("sc-bWOGAC letJNI"): # loop each product 
		Teams_list.append({ 
			"id": teams.find(class_="sc-iOeugr dKtMje").get("img scr"), 
			"name": teams.find("><").text.strip(), 
			"button": teams.find(class_="MuiButtonBase-root MuiButton-root MuiButton-text jss8 jss51").text.strip(),
			"stats_1": teams.find(class_="MuiButtonBase-root MuiButton-root MuiButton-text jss8 jss51").get("sc-cuOiQm bVPxmg"), 
			"stats_2": teams.find(class_="MuiButtonBase-root MuiButton-root MuiButton-text jss8 jss51").get("sc-cuOiQm sc-bTtZEv bVPxmg dyerwB"), 
			
		}) 
	return Teams_list


def store_results(list_of_lists): 
	Teams_list = sum(list_of_lists, []) # flatten lists 
 
	with open("Teams.csv", "w") as Teams_file: 
		# get dictionary keys for the CSV header 
		fieldnames = Teams_list[0].keys() 
		file_writer = csv.DictWriter(Teams_file, fieldnames=fieldnames) 
		file_writer.writeheader() 
		file_writer.writerows(Teams_list) 
 
list_of_lists = [ 
	extract_details(page) 
	for page in pages 
] 
store_results(list_of_lists)


