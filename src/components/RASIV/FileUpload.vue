<template
    v-slot:activator="show">
    <v-file-input
        show-size
        counter
        multiple
        label="File input"
    ></v-file-input>
</template>

<script>
export default {
    name: 'FileUpload',
    props: {
        show: false
    }
}
</script>
            