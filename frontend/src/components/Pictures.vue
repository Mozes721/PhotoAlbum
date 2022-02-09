<template>
  <main>
     <table class="table"> 
      <thead>
        <th>Headline</th>
        <th>Date</th>
        <th>Picture</th>
      </thead> 
       <tbody>
        <tr v-for="photo in photos" :key="photo.id">
          <td>{{photo.headline}}</td>
          <td>{{photo.pub_date}}</td>
          <td>{{photo.image}}</td>
        </tr>
      </tbody>
     </table>
 
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
