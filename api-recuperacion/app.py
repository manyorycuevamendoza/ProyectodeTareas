from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api


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
app.config['MYSQL_DATABASE_HOST'] = '44.208.124.18' # IP de base de datos
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



class Escribir_correo(Resource):
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
            usuario=cursor.fetchall()


            if usuario==None:
                result=jsonify({'success':False})   

            else:
                result=jsonify({'success':True})    

            
        except Exception as e:
            print(e)
            return result
        finally:
            cursor.close() 
            conn.close()
            return result

        
        







#API resource routing
api.add_resource(Login,'/login/async',endpoint='agregar_tarea')
#api.add_resource(Escribir_correo,'/recuperar/correo/<string:correo_usuario>',endpoint='recuperar')
#api.add_resource(Escribir_celular,'/recuperar/celular/<string:celular>',endpoint='recuperar')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)