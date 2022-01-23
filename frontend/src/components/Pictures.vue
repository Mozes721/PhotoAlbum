<template>
  <div>
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
          <td>{{photo.pub_date}}</td>
          <td>{{photo.image}}</td>
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
    var response = await fetch('http://localhost:8000/api/photos/');
    this.photoalbum = await response.json();
    console.log(this.photoalbum)
  },
  methods: {
    async createAlbum() {

    }
  }

}
</script>
