<script>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from './components/HelloWorld.vue';
import Perfile from './components/Perfil.vue';
import Tareas from './components/Tareas.vue';
import Pendiente from './components/Pendiente.vue';
import Papelera from './components/Papelera.vue';
import Configuracion from './components/Configuracion.vue';
import Login from './components/login.vue';
import router from "./router/index.js";




export default {
  name: 'App',
  components: {
    HelloWorld,
    Login,
    Perfile,
    Pendiente,
    Configuracion,
    Papelera,
    RouterLink,
    RouterView,
    Tareas,
  },
  data() {
    return {
      loggedIn: false,
      access:false, //para acceder a recuperar cuenta y registrarse
      access1:false, //para saber si desea crear una cuenta
      recuperar_correo:false, //para saber si quiere recuperar por correo (solo cuando access es true)
      opciones_usuario:0,
    }
  },
  created() {
    if (sessionStorage.getItem('user')) {
      this.loggedIn = true;
    }
   /* if(sessionStorage.getItem('contra') == null){
      this.loggedIn = true;
      
    }*/
  },
  methods: {
    onUserLogin() {
      this.loggedIn = true;
    },
    onUserLogout() {
      this.loggedIn = false;
      this.access=false;
      this.access1=false;
      this.opciones_usuario=0;
      router.push({path:"/Login"});
    },
    onUsercontra() {
      this.loggedIn =false;
    },

    onUserTareas(){ //para visualizar tareas
      console.log("visualizar tareas");
      this.opciones_usuario=1;
      
    },
    onUserperfil(){ //para visualizar perfil
      console.log("visualizar perfil");
      this.opciones_usuario=0;
    },
    onUserconfiguracion(){ //para visualizar configuracion
      console.log("visualizar configuracion");
      this.opciones_usuario=3;
    },
    onUserpapelera(){ //para visualizar papelera
      console.log("visualizar papelera");
      this.opciones_usuario=4;
    },
    onUsercrearpendiente(){ //para crear pendiente
      console.log("crear pendiente");
      this.opciones_usuario=2;
    },

    acceder(){
      this.access=true;
    },

    acceder1(){
      this.access1=true;
    },

    cambiar_metodo_recuperacion(){
      this.recuperar_correo=!this.recuperar_correo;
    }
  }
};

router.beforeEach((to, from, next) => {
  if (!sessionStorage.getItem('user')){ //en caso no haya accedido el usuario
    /*
    if (to.name==="cuenta"){
      acceder();
    }
    else if(to.name=="contrasena"){
      acceder();
    }
    */
  
    
    if (to.name!="Login"  && to.name!="cuenta" && to.name!="contrasena" && to.name!="correo"){
      next({name:'Login'});
    }


     
    /*
    if ((to.name==="cuenta" || to.name==="contrasena" || to.name=="correo") && to.name!="login"){
      this.access=false;
      next({name:"Login"});
    }
    else if (to.name!="Login"){
      next({name:"Login"});
    }
    */
  } 
  
  next(); //usuario ya accedió
  
  
  
  
  
  
});

</script>

<template>


    <div v-if="(opciones_usuario===0)">
      <img class="imagen" alt="imag1_" v-if="(!access && !access1) && !loggedIn" src="./assets/img1.jpg" >
      <img class="imagen1" alt="imag2_" v-if="(!access && !access1) && !loggedIn" src="./assets/qr.jpg" >
  
  
  <div class="hello">
    <HelloWorld v-if="!loggedIn" msg="Mis tareas"></HelloWorld>
  </div>
  
    <div class="login">
      <Login v-if="!loggedIn && (!access && !access1)" @user-login="onUserLogin"></Login>
      <Perfile  v-if="loggedIn" @user-logout="onUserLogout" @ver-tareas="onUserTareas" @crear-pendiente="onUsercrearpendiente" @ver-configuracion="onUserconfiguracion" @ver-papelera="onUserpapelera"></Perfile>

      
    </div>
      <div class="wrapper" v-if="(!access && !access1) && !loggedIn">
      <nav>
        <RouterLink  to="/Contrasena" v-on:click="acceder()">¿Olvidaste tu contraseña?</RouterLink>
        <RouterLink  to="/Cuenta" v-on:click="acceder1()">Crear cuenta</RouterLink>
        
      </nav>
    </div>
    
    <RouterView/>
    <div v-if="(!access1 && access)"> <!--en caso se desea recuperar (por correo o celular)-->
      <RouterLink  to="/RecuperarCorreo" v-if="!recuperar_correo" v-on:click="cambiar_metodo_recuperacion()">Recuperar por correo</RouterLink>

      <RouterLink  to="/Contrasena" v-else v-on:click="cambiar_metodo_recuperacion()">Recuperar por celular</RouterLink>
    </div>
    </div>
    <div v-else>

      <Tareas v-if="opciones_usuario===1" @user-logout="onUserLogout" @user-perfil="onUserperfil" ></Tareas>
      <Pendiente v-if="opciones_usuario===2" @user-logout="onUserLogout" @user-perfil="onUserperfil" ></Pendiente>
      <Configuracion v-if="opciones_usuario===3" @user-logout="onUserLogout" @user-perfil="onUserperfil" ></Configuracion>
      <Papelera v-if="opciones_usuario===4" @user-logout="onUserLogout" @user-perfil="onUserperfil" ></Papelera>


      <RouterView/>
    </div>


  
</template>





<style>
.login {
  margin-top: 100px;
  flex:left;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 150px;
}

.imagen{
 
  width: 550px;
  float: right;
  padding: 60px;
  margin: 200px;
  
   
}

.imagen1{
 
  width: 600px;
  float: right;
  padding: 150px;
  margin: 70px;
  margin-top: -1000px;
   
}

</style>

<style scoped>
nav {
  width: 100%;
  font-size: 20px;
  text-align: center;
  margin-top: 6rem;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

</style>
