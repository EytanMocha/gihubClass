from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("C:\\Users\IBI-LAP\Downloads\chromedriver_win32\chromedriver"))
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
print(driver.title)
driver.implicitly_wait(5)
try:
    tag_name = driver.find_element(By.ID, "user")
    print(tag_name.is_enabled())
    print(tag_name.get_attribute("outerHTML"))
    print(tag_name.accessible_name)
except Exception as e:
    print(e)
