<template>
  <main>
      <nav class="mt-10 px-6 ">
              <a class="hover:text-gray-800 hover:bg-gray-100 flex items-center p-2 my-6 transition-colors dark:hover:text-white dark:hover:bg-gray-600 duration-200  text-gray-600 dark:text-gray-400 rounded-lg" v-for="(album) in this.albums" :key="album.id">
                <div class="grid">
                <span class="mx-4 text-lg font-normal cursor-pointer" @click="albumSelect(album)">
                        {{album.name}}
                    </span>
                    <span class="mx-4 text-lg font-normal cursor-pointer" @click="Delete()">
                      <router-link to="/delete-album"  class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-red-700 rounded-lg hover:bg-red-800 focus:ring-4 focus:ring-red-300 dark:bg-red-600 dark:hover:bg-blue-red dark:focus:ring-blue-red">
                          Delete
                          <img class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" src='../../assets/delete.png' />
                      </router-link>
                    </span>
                
                </div>
                </a>
                <router-link to="/add-album" class="flex h-1-4 justify-center items-center w-1-3 ">
                  <div class="items-center ">
                    <img class="ml-2 -mr-1 w-8 h-8 hover:bg-green-400" fill="currentColor" viewBox="0 0 20 20" src='../../assets/plus.png' />
                  </div>
                </router-link>
            </nav>
  </main>
</template>

<style>

</style>
<script>
import Pictures from '../components/Pictures.vue'

export default {
  name: 'Albums',
  components: {
    Pictures,
  },
  data() {
    return {
      albums: [],
      showModal:false
    }
  },
  async created() {
	  try {
		    const response = await fetch('http://localhost:8000/api/albums/')
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
        this.albums = await response.json()
    }
    catch (err) {
        console.log(err);
    }
  },
  methods: {
    albumSelect(album) {
      this.$emit('changeAlbum', album.id)
    },
    Delete() {
      this.showModal = true;
    }
  }
}
</script>