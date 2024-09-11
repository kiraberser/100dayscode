from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#Keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
    

events = {
    index - 1: {
        'time': "2024-" + driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{index}]/time').text,
        'name': driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{index}]/a').text
    }
    for index in range(1, 6)
}
print(events)


time.sleep(2)







#price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#dirver.find_element(By.NAME, value="q")
#driver.find_element(By.ID, value="submit")
#driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
#driver.find_elements()
#price_dollar2 = driver.find_element(By.XPATH, value='//*[@id="priceBlock-outsideOfForm_feature_div"]/div/div/span[1]/span[2]/span[2]')
#.get_attribute("placeholder")    .tag_name    .size  
#print(f"The price is {price_dollar2.text}.{price_cents.text}")

driver.quit()