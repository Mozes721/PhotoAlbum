<template>
  <div id="app">
    <nav class="bg-indigo-700 shadow-lg">
        <div class="sm:flex justify-around">
          <span class="text-white font-semibold tracking-tight text-3xl font-bold p-3">PhotoAlbum</span>
        </div>
    </nav>
    <div class="grid grid-cols-5 gap-2 min-h-screen  divide-gray-400">
      <div class="bg-gray-50 border-r border-gray-200">
          <Albums @changeAlbum="updateAlbum" />
      </div>
      <div class="col-span-4 bg-gray-50 border-r border-gray-200">
          <Pictures :album="this.selectedAlbum"/>
      </div>
    </div>
  </div>
</template>

<style>

</style>
<script>
import Albums from './components/Albums.vue'
import Pictures from './components/Pictures.vue'
export default {
  name: 'App',
  components: {
    Albums,
    Pictures
  },
  data() {
    return {
      selectedAlbum: ''
    }
  },
  methods: {
    updateAlbum(value) {
      this.selectedAlbum = value 
    }
  }
}
</script>