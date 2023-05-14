<template>
    <div class="botone2">
        <button class="btn btn-link" @click="onLogout">Inicio</button>
    </div>
    <div class="botone1">
        <button class="btn btn-link" @click="onPerfil">Atrás</button>
    </div>
    <div class="main">
        <table class="table bg-warning">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Descripción</th>
                    <th>Tipo de Tarea</th>
                    <th>Fecha Inicio</th>
                    <th>Fecha Límite</th>
                    <th>Eliminar</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(todo, index) in todos" :key="index">
                    <td class="table-warning">
                        {{ index + 1 }}
                    </td>
                    <td class="table-warning">
                        {{ todo.descripcion }}
                    </td>

                    <td class="table-warning">
                        {{ todo.tipo }}
                    </td>

                    <td class="table-warning">
                        {{ todo.fecha_inicio }}
                    </td>

                    <td class="table-warning">
                        {{ todo.fecha_limite }}
                    </td>

                    <td class="table-warning">
                        <svg @click="onDeleteTodo" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                            <path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                        </svg>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
  </template>
  
  <script>

  const checkExpired = (date) => {
    const expired = 8.64e+7;
    const now = new Date();
    const itemDate = new Date(date);
    const difference = now - itemDate;
    return difference >=0 || (difference < 0 && Math.abs(difference) < expired);
  };
  

  export default {
    name: 'TodoMain',
    data() {
        return {
            newTodo: "",
            todos: [],
            newDate: ""
        }
    },
    methods: {
        onLogout() {
             this.$emit('user-logout');
             sessionStorage.removeItem('user');
        },

        onPerfil() {
             this.$emit('user-perfil');
             
         },

        onTodoInput(e) {
            //console.log(e.target.value);
            this.newTodo = e.target.value;
        },
        onDateInput(e) {
            this.newDate = e.target.value;
        },
        onAddTodo() {   
            this.todos.push({"description": this.newTodo, "date": this.newDate, "isExpired": checkExpired(this.newDate)});
            this.newTodo = "";
            this.newDate = "";
            localStorage.setItem(sessionStorage.getItem("user"), JSON.stringify(this.todos));
        },
        onDeleteTodo(e) {
            const rowToDelete = e.target.parentElement.parentElement.children[0].innerText;

            //se obtiene un id relacionado
            let id=rowToDelete-1;

            console.log(this.todos[id]);
            const tarea_a_eliminar=this.todos[id];

            const tipo=tarea_a_eliminar.tipo;

            const nombre=tarea_a_eliminar.descripcion;

            const usuario=sessionStorage.getItem('user');

            const url="http://localhost:5000/borrar/tarea/"+usuario+"/"+tipo+"/"+nombre;
            
            console.log(url);

            fetch(url,{
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                }
            });

            
            this.todos.splice(rowToDelete-1, 1);
            localStorage.setItem(sessionStorage.getItem("user"), JSON.stringify(this.todos));
            
        }
    },

    created() {
    const usuario=sessionStorage.getItem("user");
    
    const url="http://LB-Proyecto-707432864.us-east-1.elb.amazonaws.com:8006/tareas_pendientes/"+usuario;

    let result=[];

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(res=>res.json())
    .then(data=>{

        let tareas=(data.tareas);
        //console.log(tareas);

        tareas.forEach(function(tarea) {
            //se obtiene cada tarea
            console.log(tarea);

            let this_tarea={"descripcion":tarea.nombre,"fecha_inicio":tarea.fecha_inicio,"fecha_limite":tarea.fecha_limite,"tipo":tarea.tipo};

            result.push(this_tarea);

            //console.log(this.todos);
        });
        console.log(result);
        this.todos=result;
        console.log("Todos: ",this.todos);
    });
    
    
   
    }
        /*
        let todos = JSON.parse(localStorage.getItem(sessionStorage.getItem("user")));*/
        /*
        let todos=JSON.parse(fetch("http://localhost:5000/tareas_pendientes/"+(sessionStorage.getItem("user"))));
        */
       /*
        if (todos) {
            this.todos = todos.map((item) => {
                /*return {
                    "description": item.description,
                    "date": item.date,
                    "isExpired": checkExpired(item.date)
                }; 
                //equivalentemente
                return {
                    ...item,
                    "isExpired": checkExpired(item.date)
                }
            });
            
        }
       */
        
}
  
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
    .main {
        width:50%;
        margin-left:25%;
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

  </style>