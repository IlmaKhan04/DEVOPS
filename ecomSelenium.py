import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize webdriver
driver = webdriver.Chrome('/Users/I527241/Downloads/chromedriver_mac64/chromedriver')

# Open URL and maximize window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

# Click on the My Account dropdown
my_account = driver.find_element("xpath", '//span[text()="My Account"]')
my_account.click()

# Click on the Register option
register = driver.find_element("link text", 'Register')
register.click()

# Fill in the registration form
first_name = driver.find_element("id", 'input-firstname')
first_name.send_keys('test_first_name')

last_name = driver.find_element("id", 'input-lastname')
last_name.send_keys('test_last_name')

email = driver.find_element("id", 'input-email')
email.send_keys('devopsassignment@test.com')

telephone = driver.find_element("id", 'input-telephone')
telephone.send_keys('012345678')

password = driver.find_element("id", 'input-password')
password.send_keys('password')

confirm_password = driver.find_element("id", 'input-confirm')
confirm_password.send_keys('password')

privacy_policy = driver.find_element("xpath", '//input[@name="agree"]')
privacy_policy.click()

# Submit the registration form
continue_button = driver.find_element("xpath", '//input[@value="Continue"]')
continue_button.click()

# Wait for registration success message (you can modify the time.sleep value as needed)
time.sleep(5)

# Search for a product
search_box = driver.find_element("name", 'search')
search_box.send_keys('iPhone')  # Replace with the desired product to search
search_box.send_keys(Keys.RETURN)

# Wait for search results (you can modify the time.sleep value as needed)
time.sleep(2)

# Click on the first search result
first_result = driver.find_element("xpath", "//div[contains(@class, 'product-thumb')]/div/div/h4/a")
first_result.click()

# Wait for the product page to load (you can modify the time.sleep value as needed)
time.sleep(2)

# Close the browser
driver.close()
