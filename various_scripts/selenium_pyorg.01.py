from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


### Test One
driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

driver.close()

# ### Test Two
# DEBUG = True
# site = "https://www.whitehouse.gov"
# driver = webdriver.Firefox()
# driver.get(site)

# if(DEBUG): print(f"title: {driver.title}")
# assert "House" in driver.title

# driver.close()