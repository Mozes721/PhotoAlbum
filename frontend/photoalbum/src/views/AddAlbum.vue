<template>
    <aside class="pt-6">
		<div class="flex justify-center">
		<form  @submit="onSubmit" class="bg-blue-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
		<div class="mb-4">
		<label class="block text-gray-700 text-sm font-bold mb-2" for="album" >
			Album Name
		</label>
		<input v-model="album" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="album" type="text" placeholder="Album Name">
		</div>
		<div class="flex items-center justify-between">
		<input class="cursor-pointer bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="submit" value="Add" name="add" />

		<router-link to="/" class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline" type="button">
			Exit
		</router-link>
		</div>
		</form>
		</div>	
	</aside>
</template>

<script>

export default {
	name: 'AddAlbum',
	data() {
		return {
			album: ''
		}
	},
	methods: {
        onSubmit(e){
                e.preventDefault()
                if(!this.album){
                    alert('Please add a album name')
                    return
                }
		console.log(this.album)
		this.$router.push('/')
		}
	}
}

</script>
