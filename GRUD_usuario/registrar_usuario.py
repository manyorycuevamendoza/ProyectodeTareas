from importaciones import *

@app.route("/login/register",methods = ['POST'])
@cross_origin()
def registrar_usuario():
    print('a')    
    body = request.get_json() #se obtiene el body pasado por fetch

    nuevoNombre=body["newUsername"]
    nuevaClave=body["newPassword"]
    nuevoCorreo=body["newEmail"]
    nuevoTelefono=body["newPhone"]
    nuevaFechadeNacimiento=body["newDate"]
    
    print(nuevoNombre,nuevoCorreo,nuevoTelefono,nuevaFechadeNacimiento,nuevaClave)
    
    nuevoUsuario=Usuario(nombre_usuario=nuevoNombre,numero_whatsapp=nuevoTelefono,correo_electronico=nuevoCorreo,clave=nuevaClave,fecha_nacimiento=nuevaFechadeNacimiento)

    print(nuevoUsuario)

    try:    
        db.session.add(nuevoUsuario)
        db.session.commit()

        result={"success":True}
    except:
        result={"success":False}

    return json.dumps(result)