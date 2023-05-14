from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api

import smtplib
from email.message import EmailMessage



#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_tareas'
app.config['MYSQL_DATABASE_HOST'] = '54.209.128.141' # IP de base de datos
app.config['MYSQL_DATABASE_PORT'] = 8010

#Initialize the MySQL extension
mysql.init_app(app)

'''

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

'''


#.-------------------------------------correo-------------------------------------.#

'''

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

@app.route('/recuperar/correo/<correo_usuario>',methods=['POST'])
@cross_origin()
def escribir_por_correo(correo_usuario):

    #se obtiene la clave asociada con el numero de celular
    usuario=Usuario.query.filter(Usuario.correo_electronico==correo_usuario).first()

 
    mensaje="Su usuario en la App🐮 es:"+ usuario.nombre_usuario+"\nSu clave en la App🐮 es: "+usuario.clave
    email=str(usuario.correo_electronico)

    #print(mensaje,email)
    
    try:
        #se envia la clave (por WhatsApp)
        correo(email,mensaje) 

        #correo("mariana.capunay@utec.edu.pe","Desde Python")
        result={"success":True}

    except KeyError:
        result={"success":False}
    return json.dumps(result)





'''

# class Escribir_correo(Resource):
    
#     def post(self,correo_usuario):
#         try:
#             conn=mysql.connect()
#             cursor=conn.cursor()

#             #se obtiene la clave asociada con el numero de celular
#             usuario=cursor.execute("SELECT * FROM usuario WHERE correo_electronico=%s",(correo_usuario))
#             conn.commit()

#             usuario=cursor.fetchall() #fetchall devuelve una lista de tuplas, por ejemplo: 
            
#             nombre_user=usuario[0][0] #usuario[0] es la primera tupla, usuario[0][0] es el segundo elemento de la tupla
#             correo_=usuario[0][2] #usuario[0] es la primera tupla, usuario[0][2] es el tercer elemento de la tupla
#             clave_user=usuario[0][3] #usuario[0] es la primera tupla, usuario[0][3] es el tercer elemento de la tupla
#             #mensaje="Su usuario en la App🐮 es:"+ nombre_user.nombre_usuario+"\nSu clave en la App🐮 es: "+clave_user.clave
#             #email=str(correo_.correo_electronico)
#             mensaje="Su usuario en la App🐮 es:"+ nombre_user+"\nSu clave en la App🐮 es: "+clave_user
#             destinatario=str(correo_)

#             #print(mensaje,email)
#             #self.correo(email,mensaje) #por que no esta funcionando? : porque no se ha importado la funcion
#             #def correo(self,destinatario,mensaje):
#             remitente = "app.pendientes.correo@gmail.com"
#             destinatario = destinatario
#                 #mensaje = "¡Hola, mundo!"
#             email = EmailMessage()
#             email["From"] = remitente
#             email["To"] = destinatario
#             email["Subject"] = "Recuperación de Cuenta"
#             email.set_content(mensaje)
#             smtp = smtplib.SMTP_SSL("smtp.gmail.com")
#             smtp.login(remitente, "zhwmsebxjhphhuvy") #contraseña generada por Gmail para la cuenta creada
#             smtp.sendmail(remitente, destinatario, email.as_string())
#             smtp.quit()

#             if cursor.fetchall():
#                 result=jsonify({"success":True})
#                 result.status_code=200

#             else:
#                 result=jsonify({"success":False})
#                 result.status_code=404
#         except Exception as e:
#             print(e)
#             result=jsonify({"success":False})
#             result.status_code=404
#         finally:
#             cursor.close()
#             conn.close()
#             return result
        

    
            



'''

class Escribir_celular(Resource):
    def escribir_por_celular(celular):

        #se obtiene la clave asociada con el numero de celular
        usuario=Usuario.query.filter(Usuario.numero_whatsapp==celular).first()

        if usuario==None:
            result={"success":False}
        
        else:
            try:
                #se envia la clave (por WhatsApp)
                notificacion("+51"+str(celular),"Su usuario en la App🐮 es:"+ usuario.nombre_usuario+"\nSu clave en la App🐮 es: "+usuario.clave) 
                result={"success":True}

            except KeyError:
                result={"success":False}
        return json.dumps(result)



@app.route("/login/async",methods=['POST'])
@cross_origin()
def login_asincrono():
    body = request.get_json() #se obtiene el body pasado por fetch
    
    nombre=body["username"]
    clave=body["password"]

    #se obtiene a un usuario asociado a traves del nombre
    usuario=Usuario.query.filter(Usuario.nombre_usuario==nombre).first()

    if usuario==None or usuario.clave!=clave:
        result={"success":False}

    else:
        result={"success":True}

    return json.dumps(result)}
'''
    
    
class Login(Resource):
    def post(self):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()

            #obtenemos el body pasado por fetch
            
            nombre=request.form["username"]
            clave=request.form["password"]

            #se obtiene a un usuario asociado a traves del nombre con mysql
            cursor.execute("SELECT * FROM usuario WHERE nombre_usuario=%s AND clave=%s",(nombre,clave))
            conn.commit()

            if cursor.fetchall():
                response = jsonify({'success':True})         
                response.status_code = 200

            else:
                response = jsonify({'success':False})         
                response.status_code = 400

            
        except Exception as e:
            print(e)
            response = jsonify({'success':False})         
            response.status_code = 400

        finally:
            cursor.close() 
            conn.close()
            return response

        
        



#API resource routing
api.add_resource(Login,'/login/async',endpoint='agregar_tarea')
#api.add_resource(Escribir_correo,'/recuperar/correo/<correo_usuario>',endpoint='recuperar')
#api.add_resource(Escribir_celular,'/recuperar/celular/<string:celular>',endpoint='recuperar')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
