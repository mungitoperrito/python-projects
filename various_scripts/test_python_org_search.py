# To run: python test_python_org_search.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    site = "http://www.python.org"

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_title(self):
        driver = self.driver
        driver.get(PythonOrgSearch.site)
        self.assertIn("Python", driver.title)

    def test_search(self):
        driver = self.driver
        driver.get(PythonOrgSearch.site)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()