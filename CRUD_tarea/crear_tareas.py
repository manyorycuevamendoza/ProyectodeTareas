from importaciones import*
@app.route("/crear_tarea/<nombre_usuario>",methods = ['POST', 'GET'])
@cross_origin()
def crear_tareas(nombre_usuario):
    body = request.get_json() #se obtiene el body pasado por fetch

    #obtiene atributos pasados por el fetch
    nombre=body["descripcion"]

    fecha_entrega=body["fecha_limite"]

   
    #notificacion
    notificacion_dia=body["RecordatorioDia"]

    notificacion_hora=body["RecordatorioHora"]

    #notificacion
    whatsapp=body["notificacion"]
    correo=body["notificacion1"]
    no_notificacion=body["notificacion2"]


    #tipo de Tarea
    academica=body["tareaAcademica"]
    trabajo=body["tareaTrabajo"] 
    hogar=body["tareaHogar"]
    otro=body["tareaOtro"]

    #obtiene la fecha actual
    fecha_inicio=datetime.date.today()

    #para notificaciones
    notificacion=''

    if whatsapp==True:
        notificacion="Whatsapp"
    
    elif correo==True:
        notificacion="Correo"
    
    elif no_notificacion==True:
        notificacion="Sin notificación"

    
    
    #para el tipo de Tarea
    tipo=''
    if academica==True:
        tipo='Tarea Académica'

    elif hogar==True:
        tipo='Tarea del Hogar'

    elif trabajo==True:
        tipo='Tarea de Trabajo'

    elif otro==True:
        tipo='Otro tipo de Tarea'


    #transormando la fecha 
    recordatorio=datetime.datetime.strptime(notificacion_dia,'%Y-%m-%d') 

    #obteniendo horas y minutos (notificacion_hora = 19:50 )
    horas=int(notificacion_hora[0:2])
    minutos=int(notificacion_hora[3:])

    #se suma la hora brindada a la fecha  (para generar recordatorio)
    recordatorio+=datetime.timedelta(hours=horas,minutes=minutos)

    #print("Recordatorio: ",recordatorio)

    #se crea la tarea
    tarea=Tarea(nombre=nombre,fecha_inicio=fecha_inicio,fecha_entrega=fecha_entrega,eliminada=False,notificacion=recordatorio,recordatorio=notificacion,usuario_nombre=nombre_usuario,tipo=tipo)


    try:
        #se intenta añadir la tarea
        db.session.add(tarea)
        db.session.commit()
        result={'success':True}
    except KeyError:
        #se reporta el error
        result={'success':False}

    return json.dumps(result)