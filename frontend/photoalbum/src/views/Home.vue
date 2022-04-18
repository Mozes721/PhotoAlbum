<template>
    <main>
	<div class="grid grid-cols-5 gap-2 min-h-screen  divide-gray-400">
	    <div class="bg-gray-50 border-r border-gray-200">
		<Albums @changeAlbum="updateAlbum" />
	    </div>
	    <div class="col-span-4 bg-gray-50 border-r border-gray-200">
		<Pictures :album="this.selectedAlbum"/>
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