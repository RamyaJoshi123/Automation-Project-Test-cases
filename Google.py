from selenium import webdriver
import unittest    #import unit test case

class GoogleSearchTest(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        PATH = "F:\chrome driver\chromedriver.exe"  #webdriver path
        cls.driver = webdriver.Chrome(PATH)

        cls.driver.implicitly_wait(10)

        cls.driver.maximize_window()  #maximize window

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")  #getting google.com link

        self.driver.find_element_by_name('q').send_keys("w3schools.com")  #passing key as w3schools.com in search bar
        self.driver.find_element_by_name("btnK").click()  #clicking on button

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")







