<template>
    

    <div class="titulo1">
    <button class="btn btn-link" @click="onLogout">Inicio</button>
    <br><br>
    <h1>Bienvenida a tu perfil {{ username }}</h1>
    </div>

<div class="titulo2">
    <h1>Pendientes</h1>
    <br><br>
</div>
    <div class="row">
    <div class="col-1">L</div>
    <div class="col-1">M</div>
    <div class="col-1">M</div>
    <div class="col-1">J</div>
    <div class="col-1">V</div>
    <div class="col-1">S</div>
    <div class="col-1">D</div>
</div>

<div class="row">
    <div class="col-1">1</div>
    <div class="col-1">2</div>
    <div class="col-1">3</div>
    <div class="col-1">4</div>
    <div class="col-1">5</div>
    <div class="col-1">6</div>
    <div class="col-1">7</div>
</div>

<div class="row">
    <div class="col-1">8</div>
    <div class="col-1">9</div>
    <div class="col-1">10</div>
    <div class="col-1">11</div>
    <div class="col-1">12</div>
    <div class="col-1">13</div>
    <div class="col-1">14</div>

</div>

<div class="row">
    <div class="col-1">15</div>
    <div class="col-1">16</div>
    <div class="col-1">17</div>
    <div class="col-1">18</div>
    <div class="col-1">19</div>
    <div class="col-1">20</div>
    <div class="col-1">21</div>

</div>

<div class="row">
    <div class="col-1">22</div>
    <div class="col-1">23</div>
    <div class="col-1">24</div>
    <div class="col-1">25</div>
    <div class="col-1">26</div>
    <div class="col-1">27</div>
    <div class="col-1">28</div>

</div>

<div class="row">
    <div class="col-1">29</div>
    <div class="col-1">30</div>
    <div class="col-1">31</div>
    <div class="col-1"></div>
    <div class="col-1"></div>
    <div class="col-1"></div>
    <div class="col-1"></div>
</div>
    <div class="botones">

    <button class="btn btn-primary" @click="onVerTareas">Visualizar tareas pendientes</button>
    <br><br>
    <button class="btn btn-primary" @click="onCrearPendiente">Crear pendiente</button>
    <br><br>
    <button class="btn btn-primary" @click="onConfiguracion">Configuración</button>
    <br><br>
    <button class="btn btn-primary" @click="onPapelera">Papelera</button>
    </div>

    
    <img class="imagen1" alt="imagen2_" src="../assets/qr.jpg">
   
  

</template>


<style scoped>
.titulo1{
    text-align: right;
    margin: -200px 0 0;
    padding: 70px;
    font-size: 30px;
    
}
.titulo2{
    text-align: left;
    margin: -200px 0 0;
    padding: 70px;
    font-size: 30px;
    
}
.row{
display: flexbox;
flex-direction: right;
justify-content: start;
margin: 400;
padding: 90;
}

.col-1{

width: 4%;
height: 27px;
border: 20px solid rgb(195, 225, 75);
text-align: right;
margin: 400;
padding: 90;
}

.botones{
    text-align: right;
    margin: -350px 0 0;
    padding: 100px;
    font-size: 20px;
}
.imagen1{
 
    width: 600px;
  float: right;
  padding: 180px;
  margin: 70px;
  margin-top: -450px;
  
}
</style>
  
  <script>
 
  export default {
    name: 'TablaUsuarios',
    props: {
    },
    data () {
        return {
            'username': ''
        }
    },
    created() {
        if (sessionStorage.getItem('user')) {
            this.username = sessionStorage.getItem('user');
        }
    },
    methods: {
            onLogout() {
                this.$emit('user-logout');
                sessionStorage.removeItem('user');
            },
            onVerTareas() {
                this.$emit('ver-tareas');
                
            },
            onCrearPendiente() {
                this.$emit('crear-pendiente');
                
            },
            onConfiguracion() {
                this.$emit('ver-configuracion');
                
            },
            onPapelera() {
                this.$emit('ver-papelera');
                
            }
        }
  }
  </script>
