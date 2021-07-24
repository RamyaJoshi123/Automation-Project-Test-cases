#import packages
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

#creating class Test
class Test(unittest.TestCase):

    @classmethod  #annotation
    def setUpClass(cls):
        PATH = "F:\chrome driver\chromedriver.exe"
        cls.driver = webdriver.Chrome(PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_admission_eligibity_post_graduate(self):   
        self.driver.get("https://www.kletech.ac.in/")
        self.driver.find_element_by_link_text("ADMISSION").click()
        self.driver.get("https://www.kletech.ac.in/admission/admission-to-post-graduate-programs/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    def test_findmca(self):   #test whether mca admission form is woking properly or not
        self.driver.get("https://www.kletech.ac.in/")
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


    @classmethod
    def tearDownClass(cls):
        print("Test completed")






