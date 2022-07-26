<template> 
<!-- Main modal -->
<div class="grid items-center justify-center h-screen ">
    <div class="relative p-4 w-full max-w-2xl h-full md:h-auto ">
        <!-- Modal content -->
        <div class="relative bg-gray rounded-lg shadow dark:bg-gray-700">
            <div class="flex justify-between items-start p-4 rounded-t border-b dark:border-gray-800 bg-blue-300">
                <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                    Terms of Service
                </h3>
            </div>
            <div class="p-6 space-y-6">
                <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
                    WARNING:If you delete this album all the corresponding pictures will be deleted with it!
                </p>
            </div>
            <div class="flex items-center p-6 space-x-2 rounded-b border-t border-gray-200 dark:border-gray-600">
                <button @click="deleteAlbum()"  type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">I accept</button>
                <router-link to="/" data-modal-toggle="defaultModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Decline</router-link>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
	name: 'DeleteAlbum',
    data() {
        return {
        albumID: this.$route.params.id
        }
    },
    methods: {
    deleteAlbum() {
        var formdata = new FormData();
        var requestOptions = {
        method: 'DELETE',
        body: formdata,
        redirect: 'follow'
        };
        fetch(`http://127.0.0.1:8000/api/albums/${this.albumID}/`, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

        setTimeout(() => this.$router.push("/"), 500);
    }
    
  }

}
</script>
