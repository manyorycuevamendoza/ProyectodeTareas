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

class AgregarTask(Resource):
    def post(self):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()
            usuario=request.form['usuario']
            tipo=request.form['tipo']
            tarea=request.form['tarea']

            update_task_cmd="""UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"""
            cursor.execute(update_task_cmd,(False,tarea,tipo,usuario))
            conn.commit()
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
        

#-----------------------------eliminar tareas---------------------------------
class DeleteTask(Resource):
    def get(self):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()
            usuario=request.form['usuario']
            tipo=request.form['tipo']
            tarea=request.form['tarea']
            update_task_cmd="""UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"""
            cursor.execute(update_task_cmd,(True,tarea,tipo,usuario))
            conn.commit()
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
    

#-----------------------------crear tareas-----------------------------
class CreateTask(Resource):
    def post(self):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()
            nombre_usuario=request.form['nombre_usuario']#nombre de usuario
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
    def post(self):
        try:
            conn=mysql.connect()
            cursor=conn.cursor()
            usuario_nombre=request.form['usuario_nombre']
            select_task_cmd="""SELECT nombre,fecha_inicio,fecha_entrega,tipo FROM tarea WHERE usuario_nombre=%s AND eliminada=%s AND fecha_entrega>=%s"""
            cursor.execute(select_task_cmd,(usuario_nombre,False,datetime.date.today()))
            tareas=cursor.fetchall()
            tareas_usuario=[]
            for tarea in tareas:
                this={"nombre":tarea[0],"fecha_inicio":tarea[1],"fecha_limite":tarea[2],"tipo":tarea[3]}
                tareas_usuario.append(this)
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'tareas':tareas_usuario})
        

#API resource routing
api.add_resource(AgregarTask,'/agregar/tarea',endpoint='agregar_tarea')
api.add_resource(DeleteTask,'/eliminar/tarea',endpoint='eliminar_tarea')
api.add_resource(CreateTask,'/crear/tarea',endpoint='crear_tarea')
api.add_resource(PendingTasks,'/pendientes/tareas',endpoint='pendientes_tareas')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)