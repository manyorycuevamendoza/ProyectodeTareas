from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import smtplib
from email.message import EmailMessage



#Create an instance of Flask
app = Flask(__name__)
CORS(app)
#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_tareas'
app.config['MYSQL_DATABASE_HOST'] = '44.205.44.157' # IP de base de datos
app.config['MYSQL_DATABASE_PORT'] = 8010

#Initialize the MySQL extension
mysql.init_app(app)

"""
@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response
"""
@app.route('/login/async', methods=['POST'])
def login():
    try:
        conn=mysql.connect()
        cursor=conn.cursor()

        #obtenemos el body pasado por fetch
        
        nombre=request.form["username"]
        clave=request.form["password"]

        #se obtiene a un usuario asociado a traves del nombre con mysql
        cursor.execute("SELECT * FROM usuario WHERE nombre_usuario=%s AND clave=%s",(nombre,clave))
        conn.commit()

        if len(cursor.fetchall())!=0:
            response = jsonify({'success':True}) 
            response.headers.add('Access-Control-Allow-Origin', '*')        

        else:
            response = jsonify({'success':False}) 
            response.headers.add('Access-Control-Allow-Origin', '*')     

        
    except Exception as e:
        print(e)
        response = jsonify({'success':False}) 
        response.headers.add('Access-Control-Allow-Origin', '*')        
        

    finally:
        cursor.close() 
        conn.close()
        return response

        
        



#API resource routing
#api.add_resource(Login,'/login/async',endpoint='login_async')
#api.add_resource(Escribir_correo,'/recuperar/correo/<correo_usuario>',endpoint='recuperar')
#api.add_resource(Escribir_celular,'/recuperar/celular/<string:celular>',endpoint='recuperar')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
