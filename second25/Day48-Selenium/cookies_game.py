from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#1.-Chrome options 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

#2.-call all the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#3.-put five second
timeout = time.time() + 5
five_time = time.time() + 60*5 

#3.-get element "cookie"
cookie = driver.find_element(By.ID, value="cookie")

#4.-Check the right-hand pane and see if are passed 5 seconds
while True:
    cookie.click()
    if time.time() > timeout:
        #Check the amount of money we have
        money = int(driver.find_element(By.ID, value="money").text)
        
        timeout = time.time() + 5
        cookie.click()
        #Get all the elements
        store = {
            items.text.replace(" ", "").replace("-", " ").split()[0]: int(items.text.replace(" ", "").replace("-", " ").split()[1].replace(",", ""))
            for items in driver.find_elements(By.CSS_SELECTOR, value="#store div b")
            if items.text.strip() and len(items.text.split()) > 1  # Verificar que hay al menos 2 partes
        }
        buy = {}
        for name, cost in store.items():
            if money > cost:
                buy[cost] = "buy" + name
        #click the most expensive one that can be affordable 
        if buy:
            higuest_price_affordable = max(buy)
            to_purchase_id = buy[higuest_price_affordable]
            driver.find_element(By.ID, value=to_purchase_id).click()
        
    #After 5 minutes end the while and printe the cookies/second
    if time.time() > five_time:
        cookies_pers = driver.find_element(By.ID, value="cps").text.split()[-1]
        print(f"Cookies per seconde: {cookies_pers}")
        break
