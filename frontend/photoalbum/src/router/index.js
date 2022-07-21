import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import AddAlbum from '@/views/AddAlbum.vue'
import AddPicture from '@/views/AddPicture.vue'
import DeleteAlbum from '@/views/DeleteAlbum.vue'

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
  },
  {
    path: '/delete-album',
    name: 'delete-album',
    component: DeleteAlbum
  },
  
]
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
