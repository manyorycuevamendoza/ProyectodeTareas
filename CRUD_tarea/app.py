from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
#from importaciones import *
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
app.config['MYSQL_DATABASE_DB'] = 'bd_tareas'
app.config['MYSQL_DATABASE_HOST'] = '44.208.124.18' # IP de base de datos
app.config['MYSQL_DATABASE_PORT'] = 8010

#Initialize the MySQL extension
mysql.init_app(app)

#en base a sql
#------------------------------agregar tareas---------------------------------
'''
@app.route("/agregar/tarea/<usuario>/<tipo>/<tarea>",methods=['POST'])
@cross_origin()
def agregar_tarea(usuario,tipo,tarea):
    #obtiene todas las tareas con ese nombre
    tareas=Tarea.query.filter(Tarea.nombre==tarea).all()
    #busca al tipo de Tarea especifico
    for t in tareas:
    if t.tipo==tipo and t.usuario_nombre==usuario: #si existe una tarea con ese nombre, tipo y usuario
            t.eliminada=False #se cambia el valor de eliminada a False
            print(t)  #se imprime la tarea

    db.session.commit()
    return json.dumps({'success':True})
'''
class AddTask(Resource):
                    #A,     matematica,A1
    def post(self,usuario,tipo,tarea): #se recibe el usuario, tipo y tarea por la url
        try:
        #se conecta a la base de datos
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            tareaprincipal=None

            #se crea la consulta para saber si existe el usuario y el tipo de tarea con el mismo nombre de las rutas
            consulta="""SELECT * FROM tarea WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"""
            cursor.execute(consulta,(tarea,tipo,usuario))
            tareas=cursor.fetchall() #obtiene todas las tareas con ese nombre
            #busca al tipo de Tarea especifico
            for t in tareas:
                if t[1]==tipo or t[2]==usuario:
                    tareaprincipal=t #si existe una tarea con ese nombre, tipo y usuario
                    break
            if tareaprincipal!=None:
                consulta="""UPDATE tarea SET eliminada=%s WHERE nombre=%s OR tipo=%s OR usuario_nombre=%s"""
                cursor.execute(consulta,(False,tarea,tipo,usuario))
                conn.commit()
                response=jsonify('Tarea actualizada exitosamente')
                response.status_code=200
                return jsonify(response)
            else:
                consulta="""INSERT INTO tarea(nombre,tipo,usuario_nombre,eliminada) VALUES(%s,%s,%s,%s)"""
                cursor.execute(consulta,(tarea,tipo,usuario,False))
                conn.commit()
                return jsonify({"status":"tarea insertada exitosamente"})       
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
            
        
#-----------------------------eliminar tareas---------------------------------

"""
//usaremos solo post para eliminar tareas y get para obtener las tareas, por ejemple
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
        except Exception as e:
            
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})
    def post(self,usuario,tipo,tarea):
        try:
        #se conecta a la base de datos
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            #se crea la consulta
            consulta="UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s"

"""

class DeleteTask(Resource):
    def get(self,usuario,tipo,tarea):
        try:
            #obtiene todas las tareas con ese nombre
            conn=mysql.connect()
            cursor=conn.cursor()
            #se crea la consulta
            cursor.execute("SELECT * FROM tarea WHERE id=%s OR (nombre=%s AND tipo=%s AND usuario_nombre=%s)",(2,tarea,tipo,usuario))
            tareas=cursor.fetchall()
            #busca al tipo de Tarea especifico
            #si existe una tarea con ese nombre, retornamos el nombre de la tarea, su tipo y su usuario
            for t in tareas:
                if t[1]==tipo and t[2]==usuario:
                    return jsonify({"nombre":t[0],"tipo":t[1],"usuario":t[2]})
            return jsonify({"status":"tarea no encontrada"})
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            


    def post(self,usuario,tipo,tarea):
        try:
        #se conecta a la base de datos
            conn=mysql.connect()
            cursor=conn.cursor()
            #se crea la consulta
            cursor.execute("SELECT * FROM tarea WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s",(tarea,tipo,usuario))

            for fila in cursor.fetchall():
                diccionario = {
                    "id":fila[0],
                    "nombre":fila[1],
                    "fecha_inicio":fila[2],
                    "fecha_limite":fila[3],
                    "recordatorio":fila[4],
                    "tipo":fila[5],
                    "usuario_nombre":fila[6],
                    "eliminada":fila[7]
                }
            
            tareaprincipal= diccionario

            if tareaprincipal!=None:
                cursor.execute("UPDATE tarea SET eliminada=%s WHERE nombre=%s AND tipo=%s AND usuario_nombre=%s",(True,tarea,tipo,usuario))
                conn.commit()
                response=jsonify('Tarea eliminada exitosamente')
                response.status_code=200
                return jsonify(response)
            else:
                return jsonify({"status":"no existe la tarea"})
        except Exception as e:
            print(e)
            
        finally:
            cursor.close()
            conn.close()
            


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
            respuesta=cursor.execute(insert_task_cmd,(descripcion,fecha_inicio,fecha_limite,False,recordatorio,notificacion,nombre_usuario,tipo))
            conn.commit()
            return jsonify(respuesta)
        except Exception as e:
            print(e)
            return jsonify({'success':False})
        finally:
            cursor.close()
            conn.close()
            return jsonify({'success':True})

        
#-----------------------------todas la tareas menos las que fueron eliminadas-----------------------------
class PendingTasks(Resource):
    def query(self,usuario_nombre):
        try:
            conn=mysql.connect()
            cursor=conn.cursor() #se crea un cursor para ejecutar comandos
            #se crea la consulta
            consulta="SELECT nombre,fecha_inicio,fecha_entrega,tipo FROM tarea WHERE usuario_nombre=%s AND eliminada=%s AND fecha_entrega>=%s"
            cursor.execute(consulta,(usuario_nombre,False,datetime.date.today()))
            tareas=cursor.fetchall()
            response=jsonify(tareas)
            response.status_code=200
            return response
        except Exception as e:
            print(e)
            
        finally:
            cursor.close()
            conn.close()
    def get(self):
        return self.query(self.usuario_nombre)
    def post(self):
        return self.query(self.usuario_nombre)


        

#API resource routing
api.add_resource(AddTask,'/agregar/tarea/<usuario>/<tipo>/<tarea>',endpoint='agregar_tarea')
api.add_resource(DeleteTask,'/eliminar_tarea/<usuario>/<tipo>/<tarea>',endpoint='eliminar_tarea')
api.add_resource(CreateTask,'/crear_tarea/<nombre_usuario>',endpoint='crear_tarea')
api.add_resource(PendingTasks,'/tareas_pendientes/<usuario_nombre>',endpoint='tareas_pendientes')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)