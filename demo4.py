from tkinter.tix import Select

from selenium import webdriver
import selenium
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.kletech.ac.in/")
print(driver.title)
link = driver.find_element_by_link_text("ACADEMICS")
link.click()
driver.get("https://www.kletech.ac.in/soce/courses/m-tech-structural-engineering/")


