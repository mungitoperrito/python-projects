from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

DEBUG = True

def test_title():
    if(DEBUG):print(f"title: {driver.title}")
    assert ("Python" in driver.title)

def test_search():
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    if(DEBUG):print(f"page_source: {driver.page_source[:20]}")
    assert ("No results found." not in driver.page_source)

if __name__ == "__main__":
    site = "http://www.python.org"
    driver = webdriver.Firefox()
    driver.get(site)
    test_title()
    test_search()
    driver.close()
