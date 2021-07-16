#Open a browser
#Go to python.org
#webpage title contagins word python

from selenium import webdriver

PATH = "F:\chrome driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://python.org")
assert 'python' in driver.title.lower()
print("passed")
driver.maximize_window()

driver.find_element_by_css_selector("#documentation > a").click()
driver.get("http://docs.python.org/3/")

