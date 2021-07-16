from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from tkinter.tix import Select
import selenium
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium .webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestMCA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PATH = "F:\chrome driver\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()







    def test_button(self):
        self.driver.get("https://www.kletech.ac.in/")
        self.driver.find_element_by_xpath('//*[@id="page"]/div[4]/div[1]/div/div/div[1]').click()

    @classmethod
    def tearDownClass(cls):
        print("Test completed")