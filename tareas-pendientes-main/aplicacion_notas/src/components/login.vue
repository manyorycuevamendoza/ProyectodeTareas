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
        onPass  wordInput(e) {
            this.loginAttempt = false;
            this.password = e.target.value;
        },
        onLogin() {
            //const url = "http://44.211.217.4:8080/login/async";
            const url = "http://LB-Proyecto-1812304456.us-east-1.elb.amazonaws.com:8007/login/async";

            /*
            const body = {
                "username": this.username,
                "password": this.password
            };
            */

            var details = {
                'username': this.username,
                'password': this.password,
            };

            var formBody = [];
            for (var property in details) {
            var encodedKey = encodeURIComponent(property);
            var encodedValue = encodeURIComponent(details[property]);
            formBody.push(encodedKey + "=" + encodedValue);
            }
            formBody = formBody.join("&");
            /*
            fetch('https://example.com/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            },
            body: formBody
            })
            */

            fetch(url, {
                method: 'POST',
                //body: JSON.stringify(body),
                body: formBody,
                //mode: 'no-cors', // Agregar el modo "no-cors"
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
                    //"Content-Type": "application/json"
                }
            }).then((resp) => resp.json())
            .then((data) => {
                this.loginAttempt = true;
                //operador ternario (ternary operator)
                // this.success = data.success ? true : false;
                console.log(this.username, " ",this.password);
                console.log(data);
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
  
