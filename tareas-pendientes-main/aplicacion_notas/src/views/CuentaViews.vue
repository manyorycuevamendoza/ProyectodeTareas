<template>
    <!--<button class="btn btn-link" @click="onLogout()">Inicio</button>-->
    <a href=':8005/Login'>Inicio</a>
    <br><br>
     
    <label for="newUsername">Nombre:</label>
    <input v-bind:value="newUsername" v-on:input="onNewUsernameInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
    
    <br><br>

    <label for="newPassword">Contraseña:</label>
    <input v-bind:value="newPassword" v-on:input="onNewPasswordInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
    
    <br><br>

    <label for="newEmail">Correo:</label>
    <input v-bind:value="newEmail" v-on:input="onNewEmailInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">

    <br><br>

    <label for="newPhone">Telefono:</label>
    <input v-bind:value="newPhone" v-on:input="onNewPhoneInput" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-30">
    
    <br><br>

    <label for="exampleInputnacimiento">Fecha de nacimiento: </label>
    <div class ="form-group">
        <input v-bind:value="newfecha" v-on:input="onNewfechanacimiento" type="date" class="form-control" id="exampleInputnacimiento" aria-describedby="nacimientoHelp" placeholder="Fecha de nacimiento:">
    </div>
    
    <br><br>

    <button v-on:click="onNewUsernameClick" class="btn btn-primary" @click="onUpdate">Registrarse</button>
    
    <div class="fail" v-if="userExists">Nombre o correo ya registrado</div>
    
    </template>
  
  
  <script>
  export default {
    name: 'TablaUsuarios',
    props: {
    },
    data () {
        return {
            usuarios: [],
            'newUsername': '',
            'newPassword': '',
            'newEmail': '',
            'newPhone': '',
            'newfecha': '',
            userExists: false,
            'username': ''

        }
    },
    
    created() {
        const url = "http://localhost:5000/users";

        fetch(url).then((res) => res.json()).then((data) => this.usuarios = data);
        
        
        if (sessionStorage.getItem('user')) {
            this.username = sessionStorage.getItem('user');
        }
        
    },
    methods: {
        onLogout() {
                //redireccion
                sessionStorage.removeItem('user');
                
            },
            onNewUsernameInput(e) {
                this.userExists = false;
                this.newUsername = e.target.value;
            },
            onNewPasswordInput(e) {
                this.userExists = false;
                this.newPassword = e.target.value;
            },
            onNewEmailInput(e) {
                this.userExists = false;
                this.newEmail = e.target.value;
            },
            onNewPhoneInput(e) {
                this.userExists = false;
                this.newPhone = e.target.value;
            },
            onNewfechanacimiento(e) {
                this.userExists = false;
                this.newfecha = e.target.value;
            },
            onNewUsernameClick() {
                const url = "http://LB-Proyecto-707432864.us-east-1.elb.amazonaws.com:8005/login/register";

                const body = {
                    "newUsername": this.newUsername,
                    "newPassword": this.newPassword,
                    "newEmail": this.newEmail,
                    "newPhone":this.newPhone,
                    "newDate":this.newfecha
                };

                //funcion register
                fetch(url, {
                    method: "POST",
                    body: JSON.stringify(body),
                    headers: {
                    "Content-Type": "application/json"
                }
                }).then((resp) => resp.json())
                .then((data) => {
                    this.newDate='';
                    this.newPassword='';
                    this.newDate='';
                    this.newPhone='';
                    this.newEmail='';
                    this.newUsername='';
                    if (data.success) {
                        this.usuarios.push({ "username": data.username, "email": data.email });
                    } else {
                        this.userExists = true;
                    }
                });
                
            },
        }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .miTabla {
        margin-left: 38%;
    }

    .fail {
        color: red;
    }
    .form-group {
        margin-right: 48%;
        margin-left: 45%;
        size:100%;
        width: 200px;
        
    }

    
  </style>
  