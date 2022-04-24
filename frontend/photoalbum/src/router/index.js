import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import AddAlbum from '@/views/AddAlbum.vue'
import AddPicture from '@/views/AddPicture.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },

  {
    path: '/add-album',
    name: 'add-album',
    component: AddAlbum
  },
  {
    path: '/add-picture/:id',
    name: 'add-picture',
    component: AddPicture,
    props: true,
  }
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
