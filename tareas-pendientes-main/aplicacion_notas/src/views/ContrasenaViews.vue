<template>
    <div> Recupera tu cuenta</div>
    <a href='http://localhost:8080/Login'>Inicio</a>


    <div class="main">
        <div class="input-group mb-3">
            <input  @input="onCelular" :value="celular" type="text" class="form-control" placeholder="Introduce tu número de celular" aria-label="Introduce tu número de celular" aria-describedby="basic-addon2">
        </div>
        <div class="input-group-append">
            <button @click="notificar" type="button" class="btn btn-primary">Recupera tu cuenta</button>
            </div>
        <br><br>
        <div v-if="success && loginAttempt" id="success">Cuenta recuperada</div>
        <div v-if="!success && loginAttempt" id="fail">Vuelve a intentarlo</div>

        <!--<a href='http://localhost:8080/RecuperarCorreo'>Recuperar por Correo</a>-->
    </div>
        

</template>

<script>

export default{
    name: 'TodoMain',
    data(){
        return{
            newTodo: '',
            celular:'',
        }
    },
    components:{
        //RouterLink,
        //RouterView
    },
    methods: {
        onCelular(e){ // el ontodoinput ayudara a 
            this.celular=e.target.value;
            this.loginAttempt=false;
        },
        notificar(){
            //localStorage.setItem(sessionStorage.getItem('user'),JSON.stringify(this.newTodo));

            //llamado a pagina
            const url = "http://localhost:5000/recuperar/celular/"+this.celular;

            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            }).then((resp) => resp.json())
            .then((data) => {
                this.celular='';
                if (data.success){
                    this.success=true;
                }
                else{
                    this.success=false;
                }
                this.loginAttempt=true;
            });
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

