# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# specifies the path to the chromedriver.exe
# driver = webdriver.Chrome(r"C:\Users\susil\Downloads\chromedriver_win32\chromedriver")
driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element(By.ID, 'session_key')


# send_keys() to simulate key strokes
username.send_keys('xxxxx@gmail.com')

password = driver.find_element(By.ID,'session_password')

# send_keys() to simulate key strokes
password.send_keys('xxxxx')
time.sleep(2.5)
log_in_button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-btn--full-width')
#
# # locate submit button by_class_id
# log_in_button = driver.find_element_by_class_id('login submit-button')
#
# # locate submit button by_xpath
# log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()
time.sleep(8.5)