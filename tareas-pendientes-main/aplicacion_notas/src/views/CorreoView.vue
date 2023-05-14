<template>
    <div> Recupera tu cuenta</div>
    <a href='http://localhost:8080/Login'>Inicio</a>


    <div class="main">
        <div class="input-group mb-3">
            <input :value="correo" @input="onCorreo" type="text" class="form-control" placeholder="Introduce tu correo" aria-label="Introduce tu correo" aria-describedby="basic-addon2">
        </div>
        <div class="input-group-append">
            <button @click="notificar" type="button" class="btn btn-primary">Recupera tu cuenta</button>
            </div>
        <br><br>
        <div v-if="success && loginAttempt" id="success">Cuenta recuperada</div>
        <div v-if="!success && loginAttempt" id="fail">Vuelve a intentarlo</div>

        <!--<a href='http://localhost:8080/Contrasena'>Recuperar por Celular</a>-->
    </div>
        

</template>

<script>

export default{
    name: 'TodoMain',
    data(){
        return{
            correo: '',
            loginAttempt:false,
        }
    },
    components:{
        //RouterLink,
        //RouterView
    },
    methods: {
        onCorreo(e){ // el ontodoinput ayudara a 
            this.loginAttempt = false;
            this.correo=e.target.value;
        },
        notificar(){

            //llamado a pagina
            const url = "http://localhost:5000/recuperar/correo/"+this.correo;

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            }).then((resp) => resp.json())
            .then((data) => {
                this.correo = '';
                if (data.success){
                    this.success=true;
                }
                else{
                    this.success=false;
                }
                this.loginAttempt=true;
            });
            
            //localStorage.setItem(sessionStorage.getItem('user'),JSON.stringify(this.newTodo));
        },
        onLogout() {
                sessionStorage.removeItem('user');
               
            },
    


    }
}


</script>


<style scoped>
.main {
    width:50%;
    margin-left:25%;
}
</style>

