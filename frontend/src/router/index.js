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
    path: '/login',
    name: 'login',
    meta: {layout: 'empty'},
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/register',
    name: 'register',
    meta: {layout: 'empty'},
    component: () => import('@/views/Register.vue')
  },
  {
    path: '/main',
    name: 'main',
    meta: {layout: 'main'},
    component: () => import('@/views/Main.vue')
  },
  {
    path: '/currency/:id',
    name: 'currency',
    meta: {layout: 'main'},
    component: () => import('@/views/Currency.vue')
  },
]

const router = new VueRouter({
  mode: "history",
  routes
})

export default router
