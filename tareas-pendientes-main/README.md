# MIS TAREAS
<p align="center"> <img src="https://user-images.githubusercontent.com/91238621/193497685-67d4208c-7837-4b68-a926-0b49b028afd0.png" width="700"> </p>

# OBJETIVOS DEL PROYECTO

Mis tareas es una aplicación web de notas que ofrece una experiencia sencilla para escribir anotaciones. No solo es simple y fácil de usar, sino que también cuenta con una lista de verificación de asuntos pendientes que puede notificarse rápidamente mediante correo electrónico o WhatsApp (depende de configuración indicada por el usuario), una función de búsqueda, respaldo de datos y funciones de restauración. Nuestra aplicación facilita muchísimo escribir notas y buscar las antiguas directamente desde tu pantalla.

# Funciones clave de Mis Tareas:
- Función de cuaderno para escribir, recolectar y capturar ideas como notas o pendientes.
- Las notificaciones te alertarán sobre notas importantes cuando llegue la fecha y hora indicada o cuando te hayas olvidado de registrar una tarea como completada. 
- Incluye notas rápidas desde cualquier lugar.
- Ordena las notas de acuerdo al tipo al que pertenezcan.
- Práctica función de búsqueda para aquellos que toman muchas notas.

Para poder restaurar tus notas, tenemos acceso a ellas, pero no compartimos la información valiosa que contengan, pues respetamos las políticas de seguridad. 
#


A continuación, se incluye el diseño inicial planteado para esta aplicación web.

## 1 . Home
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193680934-aaf9dd97-5b85-4ecb-a53a-851cfd134518.png" width="700"> </p>


Desde esta ventana básicamente se podrá acceder a una cuenta (previamente registrada), registrarse y, además, se tiene la opción de enviar la contraseña (en caso el usuario la olvide) a través del correo o el número de celular que el usuario proporcionó al momento de registrarse.


### Recuperar contraseña
Esta serán las ventanas a la que el usuario se podrá redireccionar en caso haya olvidado la contraseña
- A través de número celular
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193681054-7c0f2ae8-fe1f-40f8-aae7-f6a4ee344919.png" width="600"]> </p>

- A través de correo electrónico
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193681356-4501cc5c-c471-4b41-86de-5cfd0aab8669.png" width="600"]> </p>




## 2. Registro
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193673477-4fdcbf07-51f9-4f16-9064-7d534fa12af8.png" width="600"]> </p>


Al momento de registrarse, el usuario deberá proporcionar (como mínimo) su correo, nombre, apellidos, fecha de nacimiento y contraseña. Lo que es opcional es proporcionar el número de celular. En caso lo proporcione, se le habilitará la opción de elegir si desea recibir notificaciones a través de la aplicación de WhatsApp o si simplemente prefiere recibirlas a través de su correo electrónico.


## 3. Perfil
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193676847-3b0ac57c-fb9a-45c9-b02d-580272b2d7a9.png" width="600"]> </p>


Al momento de acceder a su cuenta, el usuario podrá visualizar su nombre y un calendario con los pendientes que tiene para el mes actual. Asimismo, podrá redirigirse a otras 4 ventanas a través los botones: "Tareas pendientes", "Crear pendientes", "Configuración" y "Papelera".


## 4. Lo que se ve al presionar el botón "Tareas pendientes"

<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193674372-14757a5b-68af-4f1b-a39f-e21e42abadb1.png" width="600"]> </p>


Al presionar el botón "Tareas pendientes", el usuario será redirigido a una página en la que podrá visualizar la descripción, fecha de inicio y fecha límite de sus pendientes. Además, contará con la opción de buscar anotaciones, cabe resaltar que esta búsqueda se realizará a través del contenido proporcionado para la descripción de cada tarea. Adicionalmente, tendrá la opción de eliminar un pendiente (en caso ya lo haya realizado) dando click en la parte superior derecha de uno, es así como automaticamente el pendiente será enviado a la papelera.


## 5. Lo que se ve al presionar el botón "Crear pendientes"
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193697357-092c4438-2f72-483b-8622-9dbdab37f885.png" width="600"]> </p>


Si lo que el usuario desea es crear un pendiente, entonces será redirigido a una página en la que podrá visualizar un formulario. Este form le permitirá ingresar datos del pendiente, como la descripción, fecha límite y (como algo opcional) definir un recordatorio a través de fecha y hora. _Cabe aclarar que se va a considerar a la fecha de inicio de una tarea como la fecha actual del registro de una_.


## 6. Lo que se ve al presionar el botón "Configuración"
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193677620-0326723b-a7e0-4cc9-bcf9-ff8595d74104.png" width="600"]> </p>

Si lo que el usuario desea configurar su perfil, entonces será redirigido a una página en la que podrá visualizar un formulario. Este form le permitirá ingresar los datos que desee modificar y estos solo van a cambiar si ingresa su correo y contraseña y actual. Esto se añade como medida de seguridad. Como segunda medida de seguridad se retornará un mensaje de "correo o contraseña incorrecta" en caso uno de estos datos no coincidan con los almacenados en la base de datos.

## 7. Lo que se ve al presionar el botón "Papelera"
<p align="center"> <img src="https://user-images.githubusercontent.com/91635108/193678826-2a8e165b-9417-43bb-93f3-e2c14b2d04e1.png" width="600"]> </p>
Si ingresa a la papelera, el usuario podrá visualizar las notas que eliminó, bien porque ya estuviesen completadas o por error, es así que tendrá la opción de retornar estas notas a las tareas pendientes.

