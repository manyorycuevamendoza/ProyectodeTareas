from importaciones import *
@app.route("/tareas_pendientes/<usuario_nombre>",methods=['GET','POST'])
@cross_origin()
def tareas_pendientes(usuario_nombre):

    tareas=Tarea.query.filter(Tarea.usuario_nombre==usuario_nombre).all()

    
    tareas_usuario=[] 

    for tarea in tareas:
        if tarea.eliminada==False and tarea.fecha_entrega>=datetime.date.today():
            this={"nombre":tarea.nombre,"fecha_inicio":tarea.fecha_inicio,"fecha_limite":tarea.fecha_entrega,"tipo":tarea.tipo}

            tareas_usuario.append(this)


    #print(result)
    return {"tareas":tareas_usuario}
    #return json.dumps(result)