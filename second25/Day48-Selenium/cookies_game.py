from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint

#1.-Chrome options 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

#2.-call all the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 5

#3.-get element "cookie"
cookie = driver.find_element(By.ID, value="cookie")

#4.-get each div that are in #store and then get the attribute id 
store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
items_id = [item.get_attribute("id") for item in store]

#5.-five seconds to click 
timeout = time.time() + 5
five_minutes = time.time() *60*5

#6.-the program run until five seconds is finished
while True:
    cookie.click()
    #7.-check if pass 5 secons
    if timeout > 5:
        #8.-text of the prices 
        prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        #9.-all prices to integer
        item_prices = []
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        #10.-create a dictiionary 
        cookie_upgrades = {}
        #11.-change money element to integer if have a comme replace it
        for n in range(len(item_prices)):
            cookie_upgrades[n] = items_id[n]
        #12.-get all the items cost and id, then check if the cookie count money is grater than cost, if it's then create a dictionary with the cost and the id 
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        #13.-search the max value of the amount that can buy
        higuest_price_affordable_upgrade = max(affordable_upgrades)
        #14.-the id of that item 
        to_purchase_id = affordable_upgrades[higuest_price_affordable_upgrade]
        #15.-click the id of that item    
        driver.find_element(by=By.ID, value=to_purchase_id).click()
        #16.-five second more 
        timeout = time.time() + 5
        #17.-check if 5 minutes are passed and print cookie per second and the total sum 
        if time.time() > five_minutes:
            cookie_per_s = driver.find_element(By.ID, value="cps").text
            print(cookie_per_s)
            break