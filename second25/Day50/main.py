from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

password = ""
email = ""

#opciones de chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = 'eager'
chrome_options.set_capability("unhandledPromptBehavior", "dismiss")  # Configura para cerrar automáticamente los diálogos
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)#service instance 
#Local Driver
driver.get("https://tinder.com/")

driver.implicitly_wait(5)

def sign_up():
    try:
        # Esperar a que el botón "sign_up" esté presente y hacer clic
        sign_up_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/div[3]/div/div[2]/button'))
        )
        sign_up_button.click()
        print("Click en Sign Up")

        # Esperar a que el botón de inicio de sesión con Facebook esté presente y hacer clic
        log_in_Facebook = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'))
        )
        log_in_Facebook.click()
        print("Click en Log In con Facebook")
    except Exception as e:
        print("No se puede hacer click en Sign Up:", e)

def facebook():
    try:
        # Cambiar a la ventana de inicio de sesión de Facebook
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        fb_login_window = driver.window_handles[1]
        driver.switch_to.window(fb_login_window)
        print("Cambió a la ventana de inicio de sesión de Facebook:", driver.title)

        # Localizar campos de email y contraseña
        input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        input_pass = driver.find_element(By.XPATH, '//*[@id="pass"]')
        
        # Ingresar email y contraseña
        input_email.send_keys(email)
        input_pass.send_keys(password)
        print("Email y contraseña ingresados")

        # Click en el botón de iniciar sesión
        button_login = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
        button_login.click()
        print("Intentando iniciar sesión en Facebook...")

        # Verificar si existe alerta de credenciales incorrectas
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="error_box"]'))
        )
        print("Credenciales incorrectas detectadas, intentando nuevamente...")

        # Reintentar enviando la contraseña
        input_pass.clear()
        input_pass.send_keys("tu_password")
        button_login.click()

    except Exception as e:
        print("Error durante el inicio de sesión de Facebook:", e)

# Ejecución de funciones
sign_up()
facebook()
#driver.find_element(By.NAME, "email_input").send_keys("admin@localhost.dev" )




