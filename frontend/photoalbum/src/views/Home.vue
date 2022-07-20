<template>
    <main>
	<div class="grid grid-cols-5 gap-2 min-h-screen  divide-gray-400">
	    <div class="bg-gray-50 border-r border-gray-200">
		<Albums @changeAlbum="updateAlbum" />
	    </div>
	    <div class="col-span-4 bg-gray-50 border-r border-gray-200">
        <main v-if="!this.selectedAlbum">
          <h3>Welcome to your own Photoalbum Storage!</h3>
          <p>Select your album or create a new one</p>
          <p>Then check your pictures and add new ones</p>
          <p>P.S you can delete albums same as pictures</p>
        </main>
        <main v-else>
          <Pictures v-bind:photos="photos" :album="this.selectedAlbum"/>
        </main>
	    </div>
	</div>
    </main>
</template>

<script>
import Albums from '../components/Albums.vue'
import Pictures from '../components/Pictures.vue'
export default {
  name: 'App',
  components: {
    Albums,
    Pictures
  },
  data() {
    return {
      selectedAlbum: '',
      photos: []
    }
  },
  async created() {
	  try {
	      const response = await fetch('http://localhost:8000/api/photos/')
    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }
    this.photos = await response.json();
    console.log("data fetched")
    }
    catch (err) {
        console.log(err);
    }
  },

  methods: {
    updateAlbum(value) {
      this.selectedAlbum = value 
    }
  }
}
</script>