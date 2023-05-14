from twilio.rest import Client
import datetime
def notificacion(numero, cuerpo):
    account_sid = 'AC2a82bb2cd8cc4e0ef5d81a059ada9d11'
    auth_token = '7c0d2d73f29eb1443f50634690cd8ec6'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body=cuerpo,
                              to='whatsapp:'+numero
                          )

    print(message.sid)



