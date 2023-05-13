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


# Get Users
class GetUsuarios(Resource):
    def _query_database(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from usuario""")#consulta
            rows = cursor.fetchall()#obtiene todos los usuarios, fetchall() obtiene todos los registros
            conn.commit()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        rows = self._query_database()
        return (jsonify(rows))
    
    def get(self):
        rows = self._query_database()
        return (jsonify(rows))
            
#Update a User
class UpdateUser(Resource): # configuraciones
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            correo=request.form["email"] #recibe parametros
            clave=request.form["password"]
            nuevo_nombre=request.form["newName"]
            nuevo_correo=request.form["newEmail"]
            nuevo_telefono=request.form["newPhone"]
            nueva_clave=request.form["newPassword"]
            consulta = """SELECT * FROM usuario WHERE correo_electronico=%s AND clave=%s"""
            rows = cursor.execute(consulta, (correo, clave))
            rows = cursor.fetchall() # obteniendo al usuario

            # obteniendo los atributos , a partir de(ejemplo):  [(1, 'Juan', 'juan@mail.com', '123456', '555-5555')]
            nombre = rows[0][0]
            #correo_electronico = rows[0][2]
            #clave = rows[0][3]
            telefono = rows[0][1]
            
            if nuevo_correo=='': #si no se aÃ±ade caracteres
                nuevo_correo=correo

            if nuevo_nombre=='': #si no se aÃ±ade caracteres
                nuevo_nombre=nombre
            
            if nuevo_telefono=='': #si no se aÃ±ade caracteres
                nuevo_telefono=telefono
            
            if nueva_clave=='': #si no se aÃ±ade caracteres
                nueva_clave=clave
                
            #se pasÃ³ un usuario vÃ¡lido -  ya se tiene al usuario

            update_user_cmd = """UPDATE usuario SET nombre_usuario=%s, numero_whatsapp=%s, correo_electronico=%s, 
                                clave=%s 
                                  where correo_electronico=%s and clave=%s""" #se actualiza al usuario
                                
            cursor.execute(update_user_cmd, (nuevo_nombre, nuevo_telefono, nuevo_correo,nueva_clave,correo,clave))
            conn.commit()
            response = jsonify({'success':True})         
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'success':False})         
            response.status_code = 400
        
        finally:
            cursor.close()
            conn.close() 
            return response
 

class CreateUser(Resource):
    def post(self):
        try: #se crea un usuario
            conn = mysql.connect()
            cursor = conn.cursor()
            nuevoNombre=request.form["newUsername"] #recibe parametros #obtenemos los datos
            nuevaClave=request.form["newPassword"]
            nuevoCorreo=request.form["newEmail"]
            nuevoTelefono=request.form["newPhone"]
            nuevaFechadeNacimiento=request.form["newDate"]
        
            #print(nuevoNombre,nuevoCorreo,nuevoTelefono,nuevaFechadeNacimiento,nuevaClave)  #verificacion 

            consulta = """insert into usuario (nombre_usuario, numero_whatsapp, correo_electronico, clave,fecha_nacimiento) 
                                values (%s, %s, %s,%s,%s)"""
            cursor.execute(consulta, (nuevoNombre, nuevoTelefono, nuevoCorreo,nuevaClave,nuevaFechadeNacimiento))
            conn.commit()
            response = jsonify({'success':True})         
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify({'success':False})         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return response 

#API resource routes
api.add_resource(GetUsuarios, '/users', endpoint='users')
api.add_resource(UpdateUser, '/configuraciones', endpoint='user')
api.add_resource(CreateUser, '/login/register', endpoint='create_user')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
