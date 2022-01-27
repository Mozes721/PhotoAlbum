<template>
  <div id="app">
    <nav class="bg-indigo-700 shadow-lg">
        <div class="sm:flex justify-around">
          <span class="text-white font-semibold tracking-tight text-3xl font-bold p-3">PhotoAlbum</span>
        </div>
      <Albums />
    </nav>
    <!-- <Pictures /> -->
    
  </div>
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
import Albums from './components/Albums.vue'
// import Pictures from './components/Pictures.vue'


export default {
  name: 'App',
  components: {
    Albums
   
  },
  data() {
  }
}
</script>

