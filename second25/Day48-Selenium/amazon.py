from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración de ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

# Inicialización del WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Cargar la página de Amazon
driver.get("https://www.amazon.com.mx/Principles-Life-Work-Ray-Dalio/dp/1501124021/?_encoding=UTF8&ref_=pd_hp_d_btf_cr_cartx")

# Esperar unos segundos para asegurar que todo el contenido cargue
time.sleep(3)

# Extraer título del producto
title = driver.find_element(By.ID, "productTitle").text

# Extraer precio usando XPath
try:
    # Usa comillas simples para evitar conflicto con las comillas dobles dentro del XPath
    price_whole = driver.find_element(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[1]").text
    price_fraction = driver.find_element(By.XPATH, "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span[2]").text
    price = f"{price_whole}"
except Exception as e:
    price = "No disponible"

# Imprimir los resultados
print(f"{title}\nPrecio: {price}")

# Esperar antes de cerrar para evitar cierre prematuro
time.sleep(5)

# Cerrar el navegador
driver.quit()
