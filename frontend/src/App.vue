<template>
  <div id="app">
    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
    <table class="table"> 
      <thead>
        <th>Album</th>
        <th>Headline</th>
        <th>Date</th>
        <th>Picture</th>
      </thead>
      <tbody>
        <tr v-for="photo in photoalbum" :key="photo.id">
          <td>{{photo.album}}</td>
          <td>{{photo.headline}}</td>
          <td>{{photo.date}}</td>
          <td>{{photo.picture}}</td>
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
    console.log(this.photoalbum)
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

