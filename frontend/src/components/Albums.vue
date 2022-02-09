<template>
      <nav class="mt-10 px-6 ">
              <a class="hover:text-gray-800 hover:bg-gray-100 flex items-center p-2 my-6 transition-colors dark:hover:text-white dark:hover:bg-gray-600 duration-200  text-gray-600 dark:text-gray-400 rounded-lg" v-for="(album) in this.albums" :key="album.id">
                <span class="mx-4 text-lg font-normal cursor-pointer" @click="albumSelect(album)">
                        {{album.name}}
                    </span>
                    <span class="flex-grow text-right">
                    </span>
                </a>
            </nav>
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
import Pictures from '../components/Pictures.vue'
export default {
  name: 'Albums',
  components: {
    Pictures
  },
  data() {
    return {
      albums: []
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/albums');
    this.albums = await response.json();
    console.log(this.albums)
  },
  methods: {
    albumSelect(album) {
      this.$emit('changeAlbum', album.id)
      console.log(album.name, album.id)
    }
  }
}
</script>
