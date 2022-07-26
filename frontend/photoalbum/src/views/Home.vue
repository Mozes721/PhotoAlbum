<template>
	<div class="grid grid-cols-5 gap-2 min-h-screen  divide-gray-400">
	    <main class="bg-gray-50 border-r border-gray-200">
		    <Albums @changeAlbum="updateAlbum" />
	    </main>
	    <div class="col-span-4 bg-gray-50 border-r border-gray-200">
        <main v-if="!this.selectedAlbum">
        <div class="pt-6 md:p-8 text-center m space-y-4">
          <blockquote>
            <p class="text-lg font-medium">
            <ul class="text-3xl font-italic mb-7">
           <li>Welcome to your own Photoalbum Storage!</li>
            <li>Select your album or create a new one</li>
            <li>Then check your pictures and add new ones</li>
            <li>P.S you can delete albums same as pictures</li>
            </ul>
            </p>
          </blockquote>
            <figcaption class="font-medium">
                <div class="text-sky-500 dark:text-sky-400">
                  Richard Taujenis
                </div>
                <div class="text-slate-700 dark:text-slate-500">
                Full Stack Developer
                </div>
          </figcaption>
        </div>
        </main>
        <main v-else>
          <Pictures v-bind:photos="photos" :album="this.selectedAlbum" v-on:getPhoto="getCurrentPhoto($event)"/>
        </main>
        </div>
    </div>
</template>

<script>
import Albums from '../components/Albums.vue'
import Pictures from '../components/Pictures.vue'
export default {
  name: 'App',
  components: {
    Albums,
    Pictures,
},
  data() {
    return {
      selectedAlbum: '',
      photos: [],
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
    },
  }
}
</script>