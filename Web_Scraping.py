
############## open website with selenium and webdriver ###################
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# URL = 'https://herenow.com/results/#/races/20899/results'
URL = 'https://www.nhl.com/standings/2022/league'

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get(URL)
sleep(10)
# spans = driver.find_element(By.TAG_NAME, "span")
# print(type(spans))
searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'team--name')]")
print(searchresults[0].text)
print(searchresults[1].text)
print(searchresults[2].text)
print(searchresults[3].text)
print(searchresults[4].text)
print(searchresults[5].text)
print(searchresults[4].text)

# datafound = []

# for i in searchresults:
#     if len(i.text) > 0:
#         datafound.append(i.text)
#     if len(datafound) > 45:
#         break

# print(datafound)