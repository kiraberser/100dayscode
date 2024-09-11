from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 5

while True:
    cookie = driver.find_element(By.ID, value="cookie")
    cursor = driver.find_element(By.ID, value="buyCursor")
    grandma = driver.find_element(By.ID, value="buyGrandma")
    factory = driver.find_element(By.ID, value="buyFactory")
    mine = driver.find_element(By.ID, value="buyMine")
    money = driver.find_element(By.ID, value="money").text
    
    buy_cursor = int(cursor.text.split()[2])
    buy_grandma = int(grandma.text.split()[2])
    buy_factory = int(factory.text.split()[2])
    buy_mine = int(mine.text.split()[2].replace(",", ""))
    
    cookie.click()
    if time.time() > timeout: 
        #Check the amount 
        if int(money) >= buy_mine and buy_mine > buy_factory:
            buy_mine.click()
        elif int(money) >= buy_factory and buy_factory > buy_grandma:
            buy_factory.click()
        elif int(money) >= buy_grandma and buy_grandma > buy_cursor:
            buy_grandma.cick()
        elif int(money) >= buy_cursor:
            cursor.click()        
        timeout = time.time() + 5