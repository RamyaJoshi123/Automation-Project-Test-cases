from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
import unittest
import time
import re


class HomePageRest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        PATH = "E:\chrome driver\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_download_brochure(self):
        self.driver.get("https://www.kletech.ac.in/")
        if self.driver.find_element_by_id("download_brochure").is_selected():
            print("pass")
        else:
            print("fail")

    def test_enrollment(self):
        self.driver.get("https://www.kletech.ac.in/")
        if self.driver.find_element_by_xpath('//*[@id="page"]/div[4]/div[1]/div/div/div[1]').is_enabled():
            print("pass")
        else:
            print("fail")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == "__main__":
        unittest.main()
