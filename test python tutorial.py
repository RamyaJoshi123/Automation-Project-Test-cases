from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
print(driver.title)
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
except:
    driver.quit()

