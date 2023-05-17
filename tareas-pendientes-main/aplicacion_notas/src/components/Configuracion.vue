<template>
    <div class="botone2">
        <button class="btn btn-link" @click="onLogout">Inicio</button>
    </div>
    <div class="botone1">
        <button class="btn btn-link" @click="onPerfil">Atrás</button>
    </div>

    <br><br>
    <div class="titulo1">       
        <u>Confirmación de seguridad</u>
    </div>
    <br><br>
    <div class="titulo3">
        <u >Actualizar datos</u>
    </div>
    <br><br>
    <div class="subtitulo">Solo complete datos a actualizar</div>
    <br><br>

    <div class="actualizardatos">
 
    <label for="newUsername">Nombre:</label>
    <input v-bind:value="newUsername" v-on:input="onNewUsernameInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
    
    <br><br>

    <label for="newEmail">Correo:</label>
    <input v-bind:value="newEmail" v-on:input="onNewEmailInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">

    <br><br>

    <label for="newPhone">Telefono:</label>
    <input v-bind:value="newPhone" v-on:input="onNewPhoneInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
    <br><br>
    <label for="newPassword">Contraseña:</label>
    <input v-bind:value="newPassword" v-on:input="onNewPasswordInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
        
    <br><br>

    <button v-on:click="onNewUsernameClick" class="btn btn-primary" @click="onUpdate">Actualizar datos</button>
    
    <div class="fail" v-if="(userExists && intento)">Ha ocurrido un error al intentar actualizar los cambios</div>
    
    <div class="access" v-if="(!userExists && intento)">Sus datos fueron actualizados con éxito</div>

    </div>
    <div class="main">
      <div class="login content-left">
        <label for="correo_">Correo actual</label>
        <br>
        <input v-bind:value="correo_" v-on:input="onCorreo" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30" type="email" placeholder="Correo electrónico">
        <br><br>

        <label for="contrasena_">Contraseña actual</label>
        <br>
        <input v-bind:value="contrasena_" v-on:input="onContrasena" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30" type="password" placeholder="Constraseña">
      
      <br><br>
      
    </div>
    </div>

    <img class="imagen1" alt="imagen2_" src="../assets/qr.jpg">
    
 </template>
 
 <script>
 export default{
     name:'ConfiguracionView',
     prop:{

     },
     data(){
         return {
             configuraciones:[],
                'newUsername': '',
                'newEmail': '',
                'newPhone': '',
                'newPassword': '',
                userExists: false,
                'contrasena_': '',
                'correo_': '',
                intento:false,
         }
     },
     methods:{
         onLogout() {
             this.$emit('user-logout');
             sessionStorage.removeItem('user');
         },
         onContrasena(e) {
             this.userExists = false;
             this.contrasena_ = e.target.value;
             this.intento=false;
            },
            onCorreo(e) {
                this.userExists = false;
                this.correo_ = e.target.value;
                this.intento=false;
                },
            onNewUsernameInput(e) {
                this.userExists = false;
                this.newUsername = e.target.value;
                this.intento=false;
            },
            onNewPasswordInput(e) {
                this.userExists = false;
                this.newPassword = e.target.value;
                this.intento=false;
            },
            onNewEmailInput(e) {
                this.userExists = false;
                this.newEmail = e.target.value;
                this.intento=false;
            },
            onNewPhoneInput(e) {
                this.userExists = false;
                this.newPhone = e.target.value;
                this.intento=false;
            },
            onNewfechanacimiento(e) {
                this.userExists = false;
                this.newfecha = e.target.value;
                this.intento=false;
            },
            onConfirmPasswordInput(e) {
                this.userExists = false;
                this.confirmPassword = e.target.value;
                this.intento=false;
            },
            onApellidoInput(e) {
                this.userExists = false;
                this.apellido = e.target.value;
                this.intento=false;
            },
            onPerfil() {
             this.$emit('user-perfil');
             
         },
         onNewUsernameClick() {
                const url = "http://LB-Proyecto-1812304456.us-east-1.elb.amazonaws.com:8005/configuraciones";
                //const url="http://LB-Proyecto-707432864.us-east-1.elb.amazonaws.com:8005/configuraciones";
                /*
                const body={
                    "password": this.contrasena_,
                    "email": this.correo_,
                    "newName": this.newUsername,
                    "newEmail": this.newEmail,
                    "newPhone": this.newPhone,
                    "newPassword": this.newPassword,
                };
                */
                var details = {
                    "password": this.contrasena_,
                    "email": this.correo_,
                    "newName": this.newUsername,
                    "newEmail": this.newEmail,
                    "newPhone": this.newPhone,
                    "newPassword": this.newPassword,
            };

            var formBody = [];
            for (var property in details) {
            var encodedKey = encodeURIComponent(property);
            var encodedValue = encodeURIComponent(details[property]);
            formBody.push(encodedKey + "=" + encodedValue);
            }
            formBody = formBody.join("&");
                fetch(url,{
                    method: 'POST',
                    body: formBody,
                    headers:{
                        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                    }
                })
                .then(res => res.json())
                .then((data) => {
                    this.newEmail = '';
                    this.newUsername = '';
                    this.newPhone = '';
                    this.newPassword = '';
                    this.contrasena_ = '';
                    this.correo_ = '';
                    this.intento=true;
                    if(data.success){
                        this.userExists = false;
                        /*
                        this.configuraciones.push({
                            "newName": this.newUsername,
                            "newEmail": this.newEmail,
                            "newPhone": this.newPhone,
                            "newPassword": this.newPassword,
                            'password': this.contrasena_,
                            'email': this.correo_,
                        });
                        */

            } else {
                this.userExists = true;
            }
        });
    },
     }
 }
 </script>
 
 <style scoped>
 .botone1{
    text-align: left;
    margin: -210px 0 0;
    padding: 70px;
    font-size: 30px;
}

.botone2{
    text-align: right;
    margin: -190px 0 0;
    padding: 70px;
    font-size: 30px;
}

.titulo1{
    text-align: left;
    margin: -200px 0 0;
    padding: 130px;
    font-size: 30px;
    
}
.main{
    margin: -500px 0 0;
    width:30%;
    margin-left:3%;
}

.titulo3{
    text-align: right;
    margin: -380px 0 0;
    padding: 130px;
    font-size: 30px;
}

.subtitulo{
    text-align: right;
    margin: -280px 0 0;
    padding: 100px;
    font-size: 20px;
}
.actualizardatos{
    text-align: right;
    margin: -200px 0 0;
    padding: 100px;
    font-size: 20px;
}

.imagen1{
 
 width: 600px;
float: right;
padding: 150px;
margin: 900px;
margin-top: -150px;

}

.access{
    color:green;
}

.fail{
    color:red;
}

 </style>
