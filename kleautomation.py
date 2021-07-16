from selenium import webdriver
import unittest

PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://www.kletech.ac.in/")
driver.find_element_by_link_text("ACADEMICS")



print("Test completed")
