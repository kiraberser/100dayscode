from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Set the settings of selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

#Create the webdriver and the link of the page
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

#Find each input field
firstName = driver.find_element(By.NAME, value='fName')
lastName = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

#Fill out the form 
firstName.send_keys("Pedro")
lastName.send_keys("Picapiedras")
email.send_keys("pedrio@gmail.com")

#click submit button
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()


