from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up driver with option to keep page open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Maximize window and go to URL
driver.maximize_window()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# Check if word Selenium appears in page title
print('Selenium' in driver.title)

# Select element with class name btn and print inner HTML
show_message_button = driver.find_element(By.CLASS_NAME, 'btn')
print(show_message_button.get_attribute('innerHTML'))

# Type given string into form input
user_message = driver.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('hello!')

# Simulate form submission
show_message_button.click()
