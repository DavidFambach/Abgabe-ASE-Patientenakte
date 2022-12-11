import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/Anmeldung',
    name: 'Anmeldung',
    component: () => import('../views/AnmeldungView.vue'),
    meta: {requiresAuth: true},
  },
  {
    path:'*',
    name:'notfound',
    redirect:'/Anmeldung'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router.beforeEach(async(to)=>{
//   if(to.name !== 'Anmeldung' && !isAuthenticated){
//     return{name:'Anmeldung'}
//   }
// })

export default router

