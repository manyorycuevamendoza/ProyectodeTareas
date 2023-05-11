from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from importaciones import *
import datetime
#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'utec'
app.config['MYSQL_DATABASE_DB'] = 'bd_api'
app.config['MYSQL_DATABASE_HOST'] = '3.231.7.144' # IP de base de datos
app.config['MYSQL_DATABASE_PORT'] = 8005

#Initialize the MySQL extension
mysql.init_app(app)

#en base a sql
#------------------------------agregar tareas---------------------------------

class AddTask(Resource):
    def post(self,usuario,tipo,tarea): #se recibe el usuario, tipo y tarea por la url
        try:
        #se conecta a la base de datos
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            #se crea la consulta
            consulta="UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"
            cursor.execute(consulta,(False,tarea,tipo,usuario))
            conn.commit()
            response=jsonify('Tarea agregada exitosamente')
            response.status_code=200
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
#-----------------------------eliminar tareas---------------------------------
class DeleteTask(Resource):
    def get(self,usuario,tipo,tarea):
        try:
        #se conecta a la base de datos
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            #se crea la consulta
            consulta="UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"
            cursor.execute(consulta,(True,tarea,tipo,usuario))
            conn.commit()
            response=jsonify('Tarea eliminada exitosamente')
            response.status_code=200
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})

#-----------------------------crear tareas-----------------------------
class CreateTask(Resource):
    def post(self,nombre_usuario):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()
            descripcion=request.form['descripcion']#nombre de la tarea
            fecha_limite=request.form['fecha_limite']#fecha limite
            recordatorio_dia=request.form['recordatorio_dia'] #fecha de recordatorio
            recordatorio_hora=request.form['recordatorio_hora'] #hora de recordatorio
            notificacion=request.form['notificacion']#tipo de notificacion
            tipo=request.form['tipo'] #tipo de tarea
            fecha_inicio=datetime.date.today()
            recordatorio=datetime.datetime.strptime(recordatorio_dia,'%Y-%m-%d') 
            horas=int(recordatorio_hora[0:2])
            minutos=int(recordatorio_hora[3:])
            recordatorio+=datetime.timedelta(hours=horas,minutes=minutos)
            insert_task_cmd="""INSERT INTO tarea (nombre,fecha_inicio,fecha_entrega,eliminada,notificacion,recordatorio,usuario_nombre,tipo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(insert_task_cmd,(descripcion,fecha_inicio,fecha_limite,False,recordatorio,notificacion,nombre_usuario,tipo))
            conn.commit()
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})

        
#-----------------------------todas la tareas menos las que fueron eliminadas-----------------------------
class PendingTasks(Resource):
    def post(self,usuario_nombre):
        try:
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            #se crea la consulta
            consulta="SELECT nombre,fecha_inicio,fecha_entrega,tipo FROM tarea WHERE usuario_nombre=%s AND eliminada=%s AND fecha_entrega>=%s"
            cursor.execute(consulta,(usuario_nombre,False,datetime.date.today()))
            tareas=cursor.fetchall()
            response=jsonify(tareas)
            response.status_code=200
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
        

#API resource routing
api.add_resource(AddTask,'/agregar/tarea/<string:usuario>/<string:tipo>/<string:tarea>',endpoint='agregar_tarea')
api.add_resource(DeleteTask,'/eliminar_tarea/<string:usuario>/<string:tarea>',endpoint='eliminar_tarea')
api.add_resource(CreateTask,'/crear_tarea/<string:nombre_usuario>',endpoint='crear_tarea')
api.add_resource(PendingTasks,'/tareas_pendientes/<string:usuario_nombre>',endpoint='tareas_pendientes')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)