<template>
	<aside class="pt-6">
		<div class="flex justify-center">
		<form @submit="onSubmit" class="bg-blue-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
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
						focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" type="file" id="formFile" accept='image/png, image/jpeg'>
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
		}
	},
	methods: {
        onSubmit(e){
                e.preventDefault()
                if(!this.headline){
                    alert('Please add a headline name')
		    console.log(`Album chosen by the name of ${this.album_id}`)
                    return
                }
		this.$router.push('/')
		},
	onFileChange(e) {
	var files = e.target.files || e.dataTransfer.files;
	if (!files.length)
		return;
	this.createImage(files[0]);
	},
	createImage(file) {
	var image = new Image();
	var reader = new FileReader();
	var vm = this;

	reader.onload = (e) => {
		vm.image = e.target.result;
	};
	reader.readAsDataURL(file);
	},
	removeImage: function (e) {
	this.image = '';
	}
	}
}

</script>
