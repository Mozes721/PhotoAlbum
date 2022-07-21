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
						focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" ref="file" type="file" id="formFile" name="image" accept='image/png, image/jpeg'>
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
			albumID: this.$route.params.id,
			headline: '',
			image: '',
			file: '',
			existingPhotos: []
		}
	},
	async created() {
	  try {
	      const response = await fetch('http://localhost:8000/api/photos/')
		
		if (!response.ok) {
		throw new Error(`Error! status: ${response.status}`);
		}
		const json = await response.json();
		this.existingPhotos = json.filter(parent_id => parent_id.albumID === this.albumID)
		console.log(this.existingPhotos)
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
                }if(this.existingPhotos.some(existingPhotos => existingPhotos.headline.toLowerCase() === this.headline.toLowerCase())){
		    alert('Picture with this type of headline already exists in this album')
		    this.new_album = ''
                    return
		}
		else {
		var formdata = new FormData();
		formdata.append("image", this.file, this.file.name);
		formdata.append("headline", this.headline);
		formdata.append("album", this.albumID);
		formdata.append("", this.file, "file");

		var requestOptions = {
		method: 'POST',
		body: formdata,
		redirect: 'follow'
		};

		fetch("http://localhost:8000/api/photos/", requestOptions)
		.then(response => response.text())
		.then(result => console.log(result))
		.catch(error => console.log('error', error));

		setTimeout(() => {  this.$router.push('/') }, 2000);
		
		}
	},
	onFileChange() {
	var files = this.$refs.file.files
	this.file = this.$refs.file.files.item(0);

	if (!files.length)
		return;
	this.createImage(this.file);
	},
	createImage(file) {

	var reader = new FileReader();
	var vm = this;
	
	reader.onload = (e) => {
		vm.image = e.target.result;
		this.image = vm.image;
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
