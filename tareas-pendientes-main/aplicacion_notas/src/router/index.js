import {createRouter,createWebHistory} from "vue-router";
const router = createRouter({
    history: createWebHistory(),
    routes: [
        /*
        {
            path: "/Hello",
            name: "Hello",
            component: () => import("../views/HelloWorldViews.vue")
        },
        */
       /*
        {
            path: "/inicio",
            name: "Inicio",
            component: () => import("../App.vue")
        },
        */
        

        {
            path: "/Login",
            name: "Login",
            component: () => import("../views/LoginViews.vue")
        },
        {
            path: "/Contrasena",
            name: "contrasena",
            component: () => import("../views/ContrasenaViews.vue")

        },
        {
            path: "/RecuperarCorreo",
            name: "correo",
            component: () => import("../views/CorreoView.vue")
        },
        {
            path: "/Cuenta",
            name: "cuenta",
            component: () => import("../views/CuentaViews.vue")
        },


        {
            path: "/Profile",
            name: "perfil",
            component: () => import("../views/PerfilView.vue")
        },
    ],
});


export default router;

