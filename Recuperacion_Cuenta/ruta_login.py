@app.route("/login/async",methods=['POST'])
@cross_origin()
def login_asincrono():
    body = request.get_json() #se obtiene el body pasado por fetch
    
    nombre=body["username"]
    clave=body["password"]

    #se obtiene a un usuario asociado a traves del nombre
    usuario=Usuario.query.filter(Usuario.nombre_usuario==nombre).first()

    if usuario==None or usuario.clave!=clave:
        result={"success":False}

    else:
        result={"success":True}

    return json.dumps(result)