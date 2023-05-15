<template>

    <div class="login content-center">
      <label for="username">Nombre: </label>
      <input v-bind:value="username" v-on:input="onUsernameInput" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-20">
      <br><br>
      <label for="password">Contraseña: </label>
      <input v-bind:value="password" v-on:input="onPasswordInput" type="password" name="password" id="password" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500  w-20">
      <br><br>

      <button type="button" class="btn btn-primary" v-on:click="onLogin">Iniciar Sesión!</button>
      <br><br>
      <div v-if="success && loginAttempt" id="success">Acceso concedido</div>
      <div v-if="!success && loginAttempt" id="fail">Contraseña o nombre incorrecto</div>
    </div>
  </template>
  
  <script>
  import router from "../router/index"
  export default {
    name: 'LoginComponent',
    props: {
    },
    data () {
        return {
            username: "",
            password: "",
            success: false,
            loginAttempt: false
        }
    },
    methods: {
        onUsernameInput(e) {
            this.loginAttempt = false;
            this.username = e.target.value;
        },
        onPasswordInput(e) {
            this.loginAttempt = false;
            this.password = e.target.value;
        },
        onLogin() {
            const url = "http://LB-Proyecto-707432864.us-east-1.elb.amazonaws.com:8007/login/async";

            const body = {
                "username": this.username,
                "password": this.password
            };

            fetch(url, {
                method: "POST",
                body: JSON.stringify(body),
                mode: 'no-cors', // Agregar el modo "no-cors"
                headers: {
                    "Content-Type": "application/json"
                }
            })//.//then((resp) => resp.json())
            .then((data) => {
                this.loginAttempt = true;
                //operador ternario (ternary operator)
                // this.success = data.success ? true : false;
                console.log('aqui');
                this.success = data.success;
                if (this.success) {
                    sessionStorage.setItem('user', this.username);
                    //añade
                    router.push({name:"perfil"});
                    this.$emit('user-login');
                }
            });
        }
    }
  }

  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    #success {
        color: green;
    }

    #fail {
        color: red;
    }
  </style>
  