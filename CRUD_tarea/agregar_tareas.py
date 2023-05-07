from importaciones import * 

@app.route("/agregar/tarea/<usuario>/<tipo>/<tarea>",methods=['POST'])
@cross_origin()
def agregar_tarea(usuario,tipo,tarea):
   #obtiene todas las tareas con ese nombre
   tareas=Tarea.query.filter(Tarea.nombre==tarea).all()
   #busca al tipo de Tarea especifico
   for t in tareas:
    if t.tipo==tipo and t.    usuario_nombre==usuario:
            t.eliminada=False 
            print(t)  

    db.session.commit()
    return json.dumps({'success':True})