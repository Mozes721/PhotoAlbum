<template>
  <main>
      <div class="box-border grid lg:grid-cols-3 md:grid-cols-2 sm:grid-cols-1 gap-1 p-4">
          <div v-for="photo in photos" :key="photo.id">
              <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
                  <a href="#">
                      <img class="rounded-t-lg object-scale-down h-48 w-96" :src='photo.image' />
                  </a>
                <div class="p-5"> 
                    <a href="#">
                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{photo.pub_date}}</h5>
                    </a>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{photo.headline}}</p>
                      <a href="#" class="inline-flex items-center py-2 px-3  font-medium image-center text-white bg-red-700 rounded-lg hover:bg-red-800 focus:ring-4 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-blue-red dark:focus:ring-blue-red">
                          Delete
                          <img class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" src='../../assets/delete.png' />
                      </a>
                </div>
              </div>
          </div>
          <div v-if="!photos.length">
            <h3>Welcome to your own Photoalbum Storage!</h3>
            <p>Select your album or create a new one</p>
            <p>Then check your pictures and add new ones</p>
            <p>P.S you can delete albums same as pictures</p>
        </div>
        <div v-else>
          <a href="#" class="flex h-1-4 justify-center items-center w-1-3">
              <img class="ml-2 -mr-1 w-14 h-14 hover:bg-green-400" fill="currentColor" viewBox="0 0 20 20" src='../../assets/plus.png' />  
          </a>
      </div>
      </div>
  </main>
   
</template>

<style>

</style>
<script>
import axios from 'axios'
export default {
  name: 'App',
  props: ['album'],
  data() {
    return {
      albums_pictures: [],
      photos: [],
    }
  },
  async created() {
	  try {
	      const response = await fetch('http://localhost:8000/api/photos/')
	  
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
    this.albums_pictures = await response.json();
    }
    catch (err) {
        console.log(err);
    }
  },
  watch: {
    async album(selected_album){
      // const selected = selected_album
      this.photos = this.albums_pictures.filter(parent_id => parent_id.album === selected_album)
      console.log(this.photos)
    }
  }
}
</script>