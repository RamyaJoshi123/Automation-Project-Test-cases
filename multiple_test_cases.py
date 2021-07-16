from selenium import webdriver
import pytest
import unittest
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium .webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Testkle(unittest.TestCase):




    @pytest.mark.lambdatest1_1
    def test_lambdatatest1_1(self):
        PATH = "F:\chrome driver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.kletech.ac.in/')
        self.driver.maximize_window()
        self.driver.find_element_by_link_text("ACADEMICS").click()
        self.driver.get("https://www.kletech.ac.in/master-of-computer-application/")
        self.driver.find_element_by_link_text("COURSE").click()
        self.driver.get("https://www.kletech.ac.in/master-of-computer-application/courses/master-of-computer-application/")
        self.driver.find_element(By.NAME, "text-186").send_keys("abc")
        self.driver.find_element(By.NAME, "tel-344").send_keys("9591658526")
        self.driver.find_element(By.NAME, "city").send_keys("bangalore")
        self.driver.find_element(By.NAME, "email-678").send_keys("abc@gmail.com")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        self.driver.find_element_by_css_selector('.wpb_wrapper div[class="footer-contact-form"] #quick_contact_submit').click()



    @pytest.mark.lambdatest1_2
    def test_enrollnow_lambdatatest1_2(self):
        PATH = "F:\chrome driver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.kletech.ac.in/')
        self.driver.find_element_by_xpath('//*[@id="page"]/div[4]/div[1]/div/div/div[1]').click()
        self.driver.find_element(By.NAME, "text-186").send_keys("abc")
        self.driver.find_element(By.NAME, "tel-344").send_keys("9591658526")
        self.driver.find_element(By.NAME, "email-678").send_keys("abc@gmail.com")
        self.driver.find_element(By.NAME, "city").send_keys("bangalore")
        self.driver.find_element(By.NAME, "course").send_keys("MCA")
        self.driver.find_element_by_name("textarea-179").send_keys("Iam looking for MCA")
        self.driver.find_element_by_id("quick_contact_submit").click()


    @pytest.mark.lambdatest1_3
    def test_downloadbrochure_lambdatatest1_3(self):
        PATH = "F:\chrome driver\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.kletech.ac.in/')
        if self.driver.find_element_by_id("download_brochure").is_selected():
            print("pass")
        else:
            print("fail")

    @classmethod
    def tearDownClass(cls):
        print("Test completed")










