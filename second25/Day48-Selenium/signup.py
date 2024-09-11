from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

#find the first name, last name, and email fields
fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

#fill out the form
fname.send_keys("Pedro")
lname.send_keys("Pica Piedra")
email.send_keys("pedriopicapiedra@gmail.com")

#Locate the "Sign Up" button. Then click on it 
button = driver.find_element(By.CSS_SELECTOR, value=".form-signin button")
time.sleep(1)
button.click()