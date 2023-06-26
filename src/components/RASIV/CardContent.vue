<template>
    <div>
        <md-card d-flex md-with-hover class="card-box">
            <md-card-area class="card-area">
                <md-card-header>
                    <div class="md-title">{{documentContent.name}}</div>
                    <div class="md-subhead">
                        <a :href="documentContent.link"></a>
                    </div>
                </md-card-header>
            
                <md-card-content class="card-content">
                    {{documentContent.summary}}
                </md-card-content>
            </md-card-area>

            <md-card-actions mt-auto>
                <div>
                    <md-button class="md-icon-button">
                        <thumbs-up @click="voteUp(documentContent.id)"></thumbs-up>
                    </md-button>
                    <md-button @click="voteDown(documentContent.id)" class="md-icon-button">
                        <thumb-down></thumb-down>
                    </md-button>
                </div>
            </md-card-actions>

        </md-card>
    </div>
</template>

<script>
import ThumbsUp from '/node_modules/vue-material-design-icons/ThumbUp.vue';
import ThumbDown from '/node_modules/vue-material-design-icons/ThumbDown.vue';
import axios from 'axios';

export default {
    props: {
        documentContent: Object
    },
    components: {
        ThumbsUp,
        ThumbDown
    },
    methods: {
        voteUp(documentId) {
            console.log("Input document ID: " + documentId)
            axios.post('/voteup', null, {
                params: {
                    documentId
                }
            })
            .then(function(response) {
                console.log("Latest document votes: ")
                console.log(response.data['data'])
            })
        },
        voteDown(documentId) {
            axios.post('/votedown', {
                documentId: documentId
            })
            .then(function(response) {
                console.log("Latest document votes: " + response.data)
            })
        },
        documentLink(name) {
            console.log("Card " + name + " has been clicked")
            return this.documentContent.link
        }
    },
}
</script>

<style lang="scss" scoped>
// @import "node_modules/material-ui-sass/material-ui.scss";

  .card-box {
    flex-direction: column;
    padding: 7px;
    width: 320px;
    height: 500px;
    margin: 10px;
    vertical-align: top;
    flex: 1;
  }

  .card-area {
    height: 90%;
  }

  .card-content {
    height: 80%;
    overflow-y: auto;
  }

</style>