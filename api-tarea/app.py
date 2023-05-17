from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
#from importaciones import *
import datetime
import json
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
app.config['MYSQL_DATABASE_HOST'] = '54.209.128.141' # IP de base de datos
app.config['MYSQL_DATABASE_PORT'] = 8010

#Initialize the MySQL extension
mysql.init_app(app)

class PendingTasks(Resource):
    def query(self, usuario_nombre):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            consulta = "SELECT * FROM tarea WHERE usuario_nombre = %s AND eliminada = 0"
            cursor.execute(consulta, (usuario_nombre))
            tareas_db = cursor.fetchall()

            # Filtrar y transformar las tareas
            tareas_usuario = []
            for tarea in tareas_db:
                tarea_dict = {
                    "nombre": tarea[1],
                    "fecha_inicio": tarea[2].strftime("%d/%m/%y"),
                    "fecha_limite": tarea[5].strftime("%d/%m/%y"),
                    "tipo": tarea[8]
                }
                tareas_usuario.append(tarea_dict)

            response = jsonify(tareas_usuario)


        except Exception as e:
            print(e)
            response = jsonify([])


        finally:
            cursor.close()
            conn.close()
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    def get(self, usuario_nombre):
        return self.query(usuario_nombre)

    def post(self, usuario_nombre):
        return self.query(usuario_nombre)

# API resource routing
api.add_resource(PendingTasks, '/tareas_pendientes/<string:usuario_nombre>', endpoint='tareas_pendientes')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)