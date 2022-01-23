import { createRouter, createWebHistory } from 'vue-router'
import Albums from '../components/Albums.vue'
import Pictures from '../components/Pictures.vue'

const routes = [
  {
    path: '/',
    name: 'Albums',
    component: Albums
  },
  {
    path: '/pictures',
    name: 'Pictures',
    component: Pictures,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
