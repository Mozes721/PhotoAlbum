<template>
  <main>
      <div class="box-border grid lg:grid-cols-3 gap-3 md:grid-cols-2 gap-2 sm:grid-cols-1 gap-1">
          <div v-for="photo in photos" :key="photo.id" class="space-x-0.5">
              <div class="max-w-sm bg-white rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
                  <a href="#">
                      <img class="rounded-t-lg object-scale-down h-48 w-96" :src='photo.image' />
                  </a>
                <div class="p-5">
                    <a href="#">
                        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{photo.pub_date}}</h5>
                    </a>
                    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">{{photo.headline}}</p>
                      <a href="#" class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-red-700 rounded-lg hover:bg-red-800 focus:ring-4 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-blue-red dark:focus:ring-blue-red">
                          Delete
                          <img class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" src='../assets/delete.png' />
                      </a>
                </div>
              </div>
        </div>
      </div>
  </main>
   
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
<script>

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
    var response = await fetch('http://localhost:8000/api/photos/');
    this.albums_pictures = await response.json();
  },
  watch: {
    async album(selected_album){
      const selected = selected_album
      this.photos = this.albums_pictures.filter(parent_id => parent_id.album === selected)
      console.log(this.photos)
    }
  }
}
</script>
