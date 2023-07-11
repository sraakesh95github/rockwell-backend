<template>
    <div class="main-container">
        <div 
            class="card-container">
            <card-content v-for="res in resources" :key="res.id" :documentContent="res">
            </card-content>
        </div>
    </div>
</template>

<script>
import CardContent from '/src/components/RASIV/CardContents.vue'

export default {
    name: "ListCards",
    props: ['resources'],
    components: {
        CardContent
    }
}
</script>

<style scoped>
.main-container {
    justify-content: center;
}

.card-container {
    /* display: flex; */
    flex-wrap: wrap;
    justify-content: left;
    max-width: 1500px;
    align-self: center;
    margin: auto;
}
</style>