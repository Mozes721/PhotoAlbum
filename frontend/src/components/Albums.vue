<template>
  <div>
    <table class="table"> 
      <thead v-for="album in albums" :key="album.id">
        <th>{{album.name}}</th>
      </thead>
    </table>
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

 
export default {
  name: 'App',
  data() {
    return {
      photoalbum: []
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/albums/');
    this.albums = await response.json();
    console.log(this.photoalbum)
  },
  methods: {
    async createAlbum() {

    }
  }

}
</script>
