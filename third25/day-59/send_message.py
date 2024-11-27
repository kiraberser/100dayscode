import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Send_Message:
    def __init__(self):
        # Obtener el correo y contraseña del archivo .env
        self.host_email = os.getenv('EMAIL_HOST_USER')
        self.host_email_password = os.getenv('EMAIL_HOST_PASSWORD')

    def send_email(self, email, name, cel, message):
        try:
            # Crear el mensaje utilizando MIME
            msg = MIMEMultipart()
            msg['From'] = self.host_email
            msg['To'] = email
            msg['Subject'] = 'Bienvenido al Blog'

            # Cuerpo del mensaje
            body = f'Name: {name.capitalize()}!\n Email: {email}\n Tel: {cel}\n Message:{message}'
            msg.attach(MIMEText(body, 'plain'))

            # Conectar al servidor SMTP y enviar el correo
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()  # Inicia la conexión segura
                connection.login(user=self.host_email, password=self.host_email_password)  # Inicia sesión
                connection.sendmail(from_addr=self.host_email, to_addrs=email, msg=msg.as_string())  # Envía el correo

            print(f"Correo enviado a {email}")

        except Exception as e:
            print(f"Error al enviar el correo: {e}")