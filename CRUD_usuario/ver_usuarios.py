from importaciones import *

@app.route("/usersjson",methods=['GET','POST'])
@cross_origin()
def all_users():
    result=[]

    usuarios=Usuario.query.all()
    print(usuarios)
    for usuario in usuarios:
        result.append(usuario.nombre_usuario)

    return json.dumps(result)