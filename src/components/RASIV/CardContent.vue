<template>
    <div>
        <md-card d-flex md-with-hover class="card-box">

            <md-card-area class="card-area">
                    <md-card-header>
                        <div @click="documentLink(documentContent)" class="md-title">{{documentContent.name}}</div>
                    </md-card-header>
                
                    <md-card-content class="card-content">
                        <div @click="documentLink(documentContent)" class="md-subheading">
                        {{documentContent.summary}}
                        </div>
                    </md-card-content>
            </md-card-area>

            <md-card-actions mt-auto>
                <div class="card-footer">
                    <md-field id="keywords">
                        <label for="movies">Keywords</label>
                        <md-select  v-model="selectedOption" @change="handleOptionSelect"  name="keywords" md-dense>
                            <md-option v-for="option in documentContent.keywords" :value="option" :key="option"> {{ option }}
                            </md-option>
                        </md-select>
                    </md-field>
                    <md-button class="md-icon-button">
                        <thumbs-up @click="voteUp(documentContent.id)"></thumbs-up>
                    </md-button>
                    <md-button @click="voteDown(documentContent.id)" class="md-icon-button">
                        <thumb-down></thumb-down>
                    </md-button>
                    <md-button @click="voteDown(documentContent.id)" class="md-icon-button">
                        <bookmark></bookmark>
                    </md-button>
                    <div class="score-box">
                        <span class="md-headline score-text">{{ moderationScore }}</span>
                        
                    </div>
                </div>
            </md-card-actions>

        </md-card>
    </div>
</template>

<script>
import ThumbsUp from '/node_modules/vue-material-design-icons/ThumbUp.vue';
import ThumbDown from '/node_modules/vue-material-design-icons/ThumbDown.vue';
import Bookmark from '/node_modules/vue-material-design-icons/Bookmark.vue';
import axios from 'axios';

export default {
    data() {
        return {
            selectedOption: '',
            moderationScore: 10
        }
    },
    props: {
        documentContent: Object
    },
    components: {
        ThumbsUp,
        ThumbDown,
        Bookmark
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
        documentLink(documentObj) {
            console.log("Card " + documentObj.name + " has been clicked")
            window.open(this.documentContent.link, '_blank')
        },
        handleOptionSelect() {
            console.log(this.selectedOption + " has been selected...")
        }
    }
}
</script>

<style lang="scss" scoped>
// @import "node_modules/material-ui-sass/material-ui.scss";

  .card-box {
    flex-direction: column;
    padding: 7px;
    max-width: 320px; //320px
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

.card-footer {
    display: flex;
}

.md-field {
    margin-top: -10px;
    margin-right: 10px;
    margin-left: 10px;
    width: 105px;
}

.score-box {
    background-color: rgb(243, 239, 239);
    height: 40px;
    width: 45px;
    justify-content: center;
    padding-top: 5px;
}
</style>