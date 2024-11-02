from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DEBUG = True
site = "https://www.whitehouse.gov"
driver = webdriver.Firefox()
driver.get(site)

if(DEBUG): print(f"title: {driver.title}")
assert "House" in driver.title

driver.close()