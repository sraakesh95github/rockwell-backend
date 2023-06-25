<template>
    <div>
        <card-content v-for="res in resources" :key="res.id" :documentContent="res">
        </card-content>
    </div>
</template>

<script>
import CardContent from './CardContent.vue'

export default {
    name: "ListCards",
    props: ['resources'],
    components: {
        CardContent
    }
}
</script>