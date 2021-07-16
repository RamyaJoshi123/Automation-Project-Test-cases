from selenium import webdriver
import unittest

PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://google.com")

driver.find_element_by_name('q').send_keys("w3schools.com")
driver.find_element_by_name("btnK").click()


print("Test completed")

