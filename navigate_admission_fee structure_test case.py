from selenium import webdriver
import selenium
PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.kletech.ac.in/")
print(driver.title)
link=driver.find_element_by_link_text("ADMISSION\FEE STRUCTURE")
link.click()
