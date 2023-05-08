# Made by Zander Collins
# Help from https://www.zenrows.com/blog/speed-up-web-scraping-with-concurrency-in-python#concurrency
# Web scapper setup 

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Zander.Collins23/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://www.nhl.com/standings/2022/league')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

for element in soup.findALL(attrs='team--name'):
    name = element.find('col-9 row 0')
    if name not in results: 
        results.append(name.text)

print(results)

