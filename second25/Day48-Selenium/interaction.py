from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#article.click()

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

search = driver.find_element(By.CSS_SELECTOR, value="#p-search a")
search.click()
searching = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
searching.send_keys("Python", Keys.ENTER)

