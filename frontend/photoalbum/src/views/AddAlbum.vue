<template>
    <aside class="pt-6">
		<div class="flex justify-center">
			<form  v-on:submit="addAlbum" class="bg-blue-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
				<div class="mb-4">
				<label class="block text-gray-700 text-sm font-bold mb-2">
					Album Name
				</label>
				<input v-model="newAlbum" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="Album Name">
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
			newAlbum: '',
			albums: []
		}
	},
	async created() {
	    await this.getAlbums();
	},
	methods: {

	async getAlbums() {
	  try {
		    const response = await fetch('http://localhost:8000/api/albums/')
	if (!response.ok) {
	throw new Error(`Error! status: ${response.status}`);
	}
		this.albums = await response.json()
		console.log(this.albums)
	}
	catch (err) {
		console.log(err);
	}
  	},
	
        async addAlbum(e) {
		e.preventDefault()
		this.newAlbum = this.newAlbum.charAt(0).toUpperCase() + this.newAlbum.slice(1)
		if(!this.newAlbum){
                    alert('Please add a album name')
                    return
                }if(this.albums.some(album => album.name.toLowerCase() === this.newAlbum.toLowerCase())){
		    alert('Album by this name already exists')
		    this.newAlbum = ''
                    return
		}
		else {
		
		var formdata = new FormData();
		formdata.append("name", this.newAlbum);

		var requestOptions = {
		method: 'POST',
		body: formdata,
		redirect: 'follow'
		};

		fetch("http://localhost:8000/api/albums/", requestOptions)
		.then(response => response.text())
		.then(result => console.log(result))
		.catch(error => console.log('error', error));

		this.newAlbum = ''
		setTimeout(() => {  this.$router.push('/') }, 2000);

	}
	
}
}
}
</script>
