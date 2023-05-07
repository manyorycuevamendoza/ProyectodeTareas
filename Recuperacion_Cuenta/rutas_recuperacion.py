from flask import render_template
from flask import Flask
from flask_cors import cross_origin,CORS
from flask import request
import json
from conexion_WhatsApp import notificacion
from conexion_Gmail import correo

@app.route('/recuperar/celular/<celular>',methods=['POST'])
@cross_origin()
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


@app.route('/recuperar/correo/<correo_usuario>',methods=['POST'])
@cross_origin()
def escribir_por_correo(correo_usuario):

    #se obtiene la clave asociada con el numero de celular
    usuario=Usuario.query.filter(Usuario.correo_electronico==correo_usuario).first()
