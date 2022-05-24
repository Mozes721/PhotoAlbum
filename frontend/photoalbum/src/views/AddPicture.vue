<template>
	<aside class="pt-6">
		<div class="flex justify-center">
		<form @submit="addPicture" class="bg-blue-100 shadow-md rounded px-8 pt-6 pb-8 mb-4" enctype="multipart/form-data">
			<div class="mb-4">
			<label class="block text-gray-700 text-sm font-bold mb-2" for="headline">
				Headline
			</label>
			<input v-model="headline" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Title name">
			</div>
			<div v-if="!image">
				<div class="mb-6">
				<label  class="form-label inline-block mb-2 text-gray-700">Input Picture</label>
						<input @change="onFileChange" class="form-control
						
						block
						w-full
						px-3
						py-1.5
						text-base
						font-normal
						text-gray-700
						bg-gray-100 bg-clip-padding
						border border-solid border-gray-300
						rounded
						transition
						ease-in-out
						m-0
						focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" ref="file" type="file" id="formFile" accept='image/png, image/jpeg'>
				<p class="text-red-500 text-xs italic">Please choose .jpg or .png image.</p>
				</div>
			</div>
			<div v-else>
				<img class="object-cover h-48 w-96" :src="image" />
				<button class="my-4 bg-yellow-500 hover:bg-yellow-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline space-y-3" @click="removeImage">Remove image</button>
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
	name: 'AddPicture',
	data() {
		return {
			album_id: this.$route.params.id,
			headline: '',
			image: '',
			file: '',
			existing_photos: []
		}
	},
	async created() {
	  try {
	      const response = await fetch('http://localhost:8000/photos/')
		
		if (!response.ok) {
		throw new Error(`Error! status: ${response.status}`);
		}
		const json = await response.json();
		this.existing_photos = json.filter(parent_id => parent_id.album_id === this.album_id)
		console.log(this.existing_photos)
		}
		catch (err) {
			console.log(err);
		}
	},
	methods: {
        async addPicture(e){
                e.preventDefault()
		console.log(this.image)
	
                if(!this.headline){
                    alert('Please add a headline name')
                    return
                }
		if(!this.image){
                    alert('Please add a image')
                    return
                }if(this.existing_photos.some(existing_photos => existing_photos.headline.toLowerCase() === this.headline.toLowerCase())){
		    alert('Picture with this type of headline already exists in this album')
		    this.new_album = ''
                    return
		}
		else {
		try {
		let formData = new FormData();
		formData.append('image', this.file)
		const response = await fetch('http://localhost:8000/photos', {
			method: "POST",
			body: JSON.stringify(
				{
				headline: this.headline,
				image: '../assets/logo.png',
				album: this.album_id,
				}),
	
			headers: {
			// 'Accept': 'application/json',
        		'Content-Type': 'multipart/form-data',
			},
			mode: "no-cors"
			});
		const json = await response.json();
		console.log(json);
		
		} catch (e) {
		// this.$router.push('/')
		console.log(this.image)
		}
		};
		},
	onFileChange() {
	var files = this.$refs.file.files
	this.file = this.$refs.file.files.item(0);
	if (!files.length)
		return;
	this.createImage(files[0]);
	},
	createImage(file) {

	var reader = new FileReader();
	var vm = this;
	
	
	reader.onload = (e) => {
		vm.image = e.target.result;
		this.image = vm.image;
		// this.file = { encodedImage: this.image }
	};
	reader.readAsDataURL(file);

	},
	removeImage: function (e) {
	this.image = '';
	this.file = '';
	}
	}
}

</script>
