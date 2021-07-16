from tkinter.tix import Select


from selenium import webdriver
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


PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.kletech.ac.in/")
print(driver.title)
driver.find_element_by_link_text("ACADEMICS").click()
driver.get("https://www.kletech.ac.in/master-of-computer-application/")
driver.find_element_by_link_text("COURSE").click()
driver.get("https://www.kletech.ac.in/master-of-computer-application/courses/master-of-computer-application/")


status=driver.find_element(By.NAME,"text-186").is_displayed()
print(status)

telephone=driver.find_element(By.NAME,"tel-344").is_displayed()
print(telephone)




driver.find_element(By.NAME,"text-186").send_keys("abc")
driver.find_element(By.NAME,"tel-344").send_keys("9591658526")
driver.find_element(By.NAME,"city").send_keys("bangalore")
driver.find_element(By.NAME,"email-678").send_keys("abc@gmail.com")


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element_by_css_selector('.wpb_wrapper div[class="footer-contact-form"] #quick_contact_submit').click()
