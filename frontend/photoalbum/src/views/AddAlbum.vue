<template>
    <aside class="pt-6">
		<div class="flex justify-center">
			<form  v-on:submit="addAlbum" class="bg-blue-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
				<div class="mb-4">
				<label class="block text-gray-700 text-sm font-bold mb-2">
					Album Name
				</label>
				<input v-model="new_album" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="Album Name">
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
			new_album: '',
			albums: []
		}
	},
	async created() {
	    await this.getAlbums();
	},
	methods: {
	
        async addAlbum(e) {
		e.preventDefault()
		this.new_album = this.new_album.charAt(0).toUpperCase() + this.new_album.slice(1)
		if(!this.new_album){
                    alert('Please add a album name')
                    return
                }if(this.albums.some(album => album.name === this.new_album)){
		    alert('Album by this name already exists')
                    return
		}
		else {
		try {
		const response = await fetch('http://localhost:8000/albums', {
			method: "POST",
			body: JSON.stringify(
				{
				name: this.new_album
				}),
			headers: {
			"Content-Type": "application/json",
		
			},
			mode: "no-cors"
			});
		const json = await response.json();
		console.log(json);
		} catch (e) {
		pass
		}
		};
		this.$router.push('/')
		}
	}
}


</script>
