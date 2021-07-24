from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys

PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://stackoverflow.com")
driver.maximize_window()

element = driver.find_element_by_name("q")
element.send_keys("selenium webdriver")
element.send_keys(Keys.ENTER)
