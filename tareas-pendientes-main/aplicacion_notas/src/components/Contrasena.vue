<template>
    <div> Recupera tu cuenta</div>
    <div class="main">
        <div class="input-group mb-3">
            <input :value="newTodo" @input="onTodoInput" type="text" class="form-control" placeholder="Introduce tu número de celular" aria-label="Introduce tu número de celular" aria-describedby="basic-addon2">
        </div>
        <div class="input-group-append">
            <button @click="onAddTodo" type="button" class="btn btn-primary">Recupera tu cuenta</button>
            </div>
    <br><br>
        <br><br>
        <div v-if="success && loginAttempt" id="success">Cuenta recuperada</div>
        <div v-if="!success && loginAttempt" id="fail">Vuelve a intentarlo</div>

    </div>
        

</template>

<script>

export default{
    name: 'TodoMain',
    data(){
        return{
            newTodo: ''
        }
    },
    methods: {
        onTodoInput(e){ // el ontodoinput ayudara a 
            this.loginAttempt = false;
            this.$emit('todo-input', e.target.value);
        },
        onAddTodo(){


            this.newTodo = '';
            //localStorage.setItem(sessionStorage.getItem('user'),JSON.stringify(this.newTodo));
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

