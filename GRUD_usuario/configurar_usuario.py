from importaciones import *

@app.route("/configuraciones",methods = ['POST'])
@cross_origin()
def configuraciones():
    body = request.get_json() #se obtiene el body pasado por fetch
    
    #obtiene parametros de body
    correo=body["email"]
    clave=body["password"]
    nuevo_nombre=body["newName"]
    nuevo_correo=body["newEmail"]
    nuevo_telefono=body["newPhone"]
    nueva_clave=body["newPassword"]

    if correo=='' or  clave=='': #verifica si el correo o la clave son vacios
        result={'success':False}
    
    elif nuevo_nombre=='' and nuevo_correo=='' and nueva_clave=='' and nuevo_telefono=='':
        #verifica si todos los atributos están vacios
        result={'success':False}

    else: #cuando se pasó el valor de al menos un atributo

        #se obtiene al usuario
        usuario=Usuario.query.filter(Usuario.correo_electronico==correo).first()

        if (usuario==None or usuario.clave!=clave):
            result={'success':False}
        
        else: 
            #se actualiza valores de atributos enviados
            if nuevo_nombre!='':
                usuario.nombre_usuario=nuevo_nombre

            if nuevo_correo!='':
                usuario.correo_electronico=nuevo_correo

            if nuevo_telefono!='':
                usuario.numero_whatsapp=nuevo_telefono
            
            if nueva_clave!='':
                usuario.clave=nueva_clave
        

            result={'success':True}

    db.session.commit()
    return json.dumps(result)