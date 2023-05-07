from email.message import EmailMessage
import smtplib

def correo(destinatario,mensaje):
    remitente = "app.pendientes.correo@gmail.com"
    destinatario = destinatario
    #mensaje = "¡Hola, mundo!"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Recuperación de Cuenta"
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")

    #descomentar para enviar mensajes por Gmail
    #smtp.login(remitente, "uvbrpawoeqiweqiz") #contraseña generada por Gmail para la cuenta creada
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

#correo("mariana.capunay@utec.edu.pe","Desde Python")