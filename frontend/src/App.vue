<template>
  <div id="app">
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    <table class="table"> 
      <thead>
        <th>Name</th>
        <th>About</th>
      </thead>
      <tbody>
        <tr v-for="photo in photoalbum" :key="photo.id">
          <td>{{photo.name}}</td>
          <td>{{photo.about}}</td>
        </tr>
      </tbody>
    </table>

  </div>
  <!-- <router-view/> -->
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
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      photoalbum: []
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/photoalbum/');
    this.photoalbum = await response.json();
  },
  methods: {
    async createAlbum() {

    }
  }
  // mounted () {
  //   axios.get('http://localhost:8000').then((response) => {
  //     console.log(response.data)
  //   })
  // }
}
</script>

