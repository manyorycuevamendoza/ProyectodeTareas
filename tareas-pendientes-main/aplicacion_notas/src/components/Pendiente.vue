<template>
    <div class="botone2">
        <button class="btn btn-link" @click="onLogout">Inicio</button>
    </div>
    <div class="botone1">
        <button class="btn btn-link" @click="onPerfil">Atrás</button>
    </div>
   <div class="titulo1">       
        <u>Añade tu tarea</u>
    </div>
    <div class="titulo3">
        <u >Pendientes</u>
    </div>

    
    <div class="row">
    <u class="col-1">L</u>
    <u class="col-1">M</u>
    <u class="col-1">M</u>
    <u class="col-1">J</u>
    <u class="col-1">V</u>
    <u class="col-1">S</u>
    <u class="col-1">D</u>
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




    <div class="titulo2">       
        <u>Tipo de tarea</u>
    </div>

    <div class="main">

<label for="exampleInputnacimiento">Fecha límite: </label>
<div class ="form-group">
<input v-bind:value="newfecha" v-on:input="onNewfechanacimiento" type="date" class="form-control" id="exampleInputnacimiento" aria-describedby="nacimientoHelp" placeholder="Fecha de nacimiento:">
</div>

<div class="input-group mb-3">
<input v-bind:value="descripcion" v-on:input="onDescripcionChange" type="text" class="form-control" placeholder="Descripción" aria-label="Descripción" aria-describedby="basic-addon2">
</div>
</div>

    <div class="radiostipo">     
    <div class="btn-group btn-group-toggle" data-toggle="buttons">
    <label class="btn btn-info">
        <input v-bind:value="TareaAcademica" v-on:input="onNewAcademico" type="radio" name="flexRadioDefault" autocomplete="off"> Tarea Académica
    </label>
    <label class="btn btn-info active">
        <input v-bind:value="TareaHogar" v-on:input="onNewHogar" type="radio" name="flexRadioDefault" autocomplete="off"> Tarea del hogar
    </label>
    <label class="btn btn-info active">
        <input v-bind:value="TareaTrabajo" v-on:input="onNewTrabajo" type="radio" name="flexRadioDefault" autocomplete="off"> Tarea de trabajo
    </label>

    <label class="btn btn-info active">
        <input v-bind:value="TareaOtro" v-on:input="onNewOtro" type="radio" name="flexRadioDefault" autocomplete="off"> Otro tipo de tarea
    </label>
</div>
</div>

    <div class="titulo4">       
        <u>Recordatorio</u>
    </div>
    <div class="main1">

        <label for="exampleInputnacimiento">día: </label>
        <div class ="form-group">
        <input v-bind:value="newdia" v-on:input="onNewdia" type="date" class="form-control" id="exampleInputdia" aria-describedby="diaHelp" placeholder="día:">
        </div>
        <div class ="form-group">
        <input v-bind:value="newhora" v-on:input="onNewhora" type="time" class="form-control" id="exampleInputhora" aria-describedby="horaHelp" placeholder="hora:">
        </div>

    </div>
    <div class="titulo5">       
        <u>Notificaciones</u>
    </div>

    

<div class="form-check0">
  <input v-bind:value="Notificacion" v-on:input="onNotificacion" class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1">
  <label class="form-check-label" for="exampleRadios1">
    WhatsApp
  </label>
</div>
<div class="form-check1">
  <input class="form-check-input" v-bind:value="Notificacion1" v-on:input="onNotificacion1" type="radio" name="exampleRadios" id="exampleRadios2">
  <label class="form-check-label" for="exampleRadios2">
    Correo
  </label>
</div>
<div class="form-check2">
  <input class="form-check-input" type="radio" v-bind:value="Notificacion2" v-on:input="onNotificacion2" name="exampleRadios" id="exampleRadios3">
  <label class="form-check-label" for="exampleRadios3">
    Deseo no recibir notificaciones
  </label>
</div>

<div class="botonnotificacion">
    <button class="btn btn-primary" @click="onAddTarea">Añadir</button>
</div>

<div class="fail" v-if="tareaExiste">Tarea ya registrada</div>
   

<img class="imagen1" alt="imagen2_" src="../assets/qr.jpg">
 </template>
 
 <script>
 export default{
     name:'PendienteView',
     props:{

     },
     data(){
         return {
            tareas:[],
            'descripcion':'',
            'newfecha':'',
            'newdia':'',
            'newhora':'',
            'TareaAcademica':'',
            'TareaHogar':'',
            'TareaTrabajo':'',
            'TareaOtro':'',
            'Notificacion':'',
            'Notificacion1':'',
            'Notificacion2':'',
            'tareaExiste':false,
            'nombre_usuario':'',
            

         }
     },
     created(){
            const url="http://localhost:5000/crear_tarea/<nombre_usuario>";
            fetch(url)
            .then(res=>res.json())
            .then(data=>{
                this.tareas=data;
            })
            if (sessionStorage.getItem('user')){
                this.nombre_usuario = sessionStorage.getItem('user');
            } 
            },
     methods:{
         onLogout() {
             this.$emit('user-logout');
             sessionStorage.removeItem('user');
         },
         onPerfil(){
                this.$emit('user-perfil');
            },
         onDescripcionChange(e){
            this.tareaExiste=false;
             this.descripcion=e.target.value;
         },
            onNewfechanacimiento(e){
                this.tareaExiste=false;
                this.newfecha=e.target.value;
            },
            onNewAcademico(){
                this.TareaAcademica=true;
                this.TareaHogar=false;
                this.TareaTrabajo=false;
                this.TareaOtro=false;
            },
            onNewHogar(){
                this.TareaAcademica=false;
                this.TareaHogar=true;
                this.TareaTrabajo=false;
                this.TareaOtro=false;
            },
            onNewTrabajo(){
                this.TareaAcademica=false;
                this.TareaHogar=false;
                this.TareaTrabajo=true;
                this.TareaOtro=false;
            },
            onNewOtro(){
                this.TareaAcademica=false;
                this.TareaHogar=false;
                this.TareaTrabajo=false;
                this.TareaOtro=true;
            },
            onNewdia(e){
                this.tareaExiste=false;
                this.newdia=e.target.value;
            },
            onNewhora(e){
                this.tareaExiste=false;
                this.newhora=e.target.value;
            },
            onNotificacion(){
                this.Notificacion=true;
                this.Notificacion1=false;
                this.Notificacion2=false;
            },
            onNotificacion1(){
                this.Notificacion=false;
                this.Notificacion1=true;
                this.Notificacion2=false;
            },
            onNotificacion2(){
                this.Notificacion=false;
                this.Notificacion1=false;
                this.Notificacion2=true;
            },
            onAddTarea(){
                const url="http://localhost:5000/crear_tarea/";
                    
                const body = {
                    "notificacion":this.Notificacion,
                    "notificacion1":this.Notificacion1,
                    "notificacion2":this.Notificacion2,
                    "tareaAcademica":this.TareaAcademica,
                    "tareaTrabajo":this.TareaTrabajo,
                    "tareaHogar":this.TareaHogar,
                    "tareaOtro":this.TareaOtro,
                    "descripcion":this.descripcion,
                    "RecordatorioDia":this.newdia,
                    "fecha_limite":this.newfecha,
                    "RecordatorioHora":this.newhora,
                };

                console.log(this.newhora)
                const usuario=sessionStorage.getItem('user');
                //enviando la tarea
                fetch(url+usuario,{
                        method:'POST',
                        body:JSON.stringify(body),
                        headers:{
                            'Content-Type':'application/json'
                        }
                    })
                    .then(res=>res.json())
                    .then((data) => {
                        this.descripcion='';
                        this.newfecha='';
                        this.newdia='';
                        this.newhora='';
                        this.TareaAcademica='';
                        this.TareaHogar='';
                        this.TareaTrabajo='';
                        this.TareaOtro='';
                        this.Notificacion='';
                        this.Notificacion1='';
                        this.Notificacion2='';
                        if(data.success){
                            console.log('Tarea añadida');    
                        
                        } else {
                            console.log('No se puede añadir tarea');
                            this.tareaExiste=true;
                        }
                    });
            },
            },
     }
 </script>
 
 <style scoped>

 .titulo1{
     text-align: left;
     margin: -200px 0 0;
     padding: 130px;
     font-size: 30px;
     
 }
 .titulo2{
     text-align: left;
     margin: -100px 0 0;
     padding: 130px;
     font-size: 30px;
     
 }
 
 .titulo3{
     text-align: right;
     margin: -310px 0 0;
     padding: 130px;
     font-size: 30px;
 }
 .titulo5{
     text-align: right;
     margin: -360px 0 0;
     padding: 130px;
     font-size: 30px;
     
 }
 
 
 
 .titulo4{
     text-align: left;
     margin: -10px 0 0;
     padding: 130px;
     font-size: 30px;
     
 }
 
 
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
 .main {
     margin: -500px 0 0;
     width:30%;
     margin-left:3%;
 }
 .main1 {
     margin: -100px 0 0;
     width:30%;
     margin-left:3%;
 }
 
 
 .radiostipo{
     margin: 300px 0 0;
     width:30%;
     margin-left:3%;
 }
 
 
 .form-check0{
     margin: -120px 0 0;
     margin-right:-70%;
     padding: 10px;
 }
 
 .form-check1{
     margin: -82px 0 0;
     margin-right:-68%;
     padding: 85px;
 }
 
 
 
 .form-check2{
     margin: -100px 0 0;
     margin-right:-80%;
     padding: 30px;
 }
 
 .botonnotificacion{
     margin: -100px 0 0;
     margin-right:-80%;
     padding: 80px;
 }
 
 .imagen1{
  
  width: 600px;
 float: right;
 padding: 150px;
 margin: 200px;
 margin-top: -500px;
 
 }
 
 .row{
 display: right;
 flex-direction: right;
 justify-content: right;
 margin: 400;
 padding: 90;
 position: relative;
 }
 
 .col-1{
 width: 4%;
 height: 27px;
 border: 20px solid rgb(95, 225, 75);
 text-align: right;
 margin: 400;
 padding: 90;
 position: relative;
 }
 
  </style>