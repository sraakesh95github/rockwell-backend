<template>
    <div>

        <v-card 
        d-flex width="350" 
        variant="tonal"
        class="card-box"
        :elevation="1">

            <v-card-item class="card-area">

                    <v-card-title>
                        <div @click="documentLink(documentContent)">{{documentContent.name}}</div>
                    </v-card-title>

            </v-card-item>
                    <!-- <v-card-text
                    class="card-content">
                        <div @click="documentLink(documentContent)" class="md-subheading">
                        {{documentContent.summary}}
                        </div>
                    </v-card-text> -->
                    
            <div 
            class="keywords">
                <v-btn
                class="mx-1 my-1"
                variant="tonal" 
                v-for="keyword in documentContent.keywords"
                :key="keyword">{{ keyword }}</v-btn>
            </div>
                
            <v-card-actions mt-auto>
                <div class="card-footer">
                    <!-- <md-field id="keywords">
                        <label for="movies">Keywords</label>
                        <md-select  v-model="selectedOption" @change="handleOptionSelect"  name="keywords" md-dense>
                            <md-option v-for="option in documentContent.keywords" :value="option" :key="option"> {{ option }}
                            </md-option>
                        </md-select>
                    </md-field> -->
                    <!-- <md-button class="md-icon-button">
                        <thumbs-up @click="voteUp(documentContent.id)"></thumbs-up>
                        <v-icon icon="fa:fas fa-lock"></v-icon>
                    </md-button> -->

                    <v-btn
                    class="ma-2"
                    icon="mdi-thumb-up"></v-btn>

                    <v-btn
                    class="ma-2"
                    icon="mdi-thumb-down"></v-btn>

                    <v-btn
                    class="ma-2"
                    icon="mdi-bookmark"></v-btn>

                    <!-- <md-button @click="voteDown(documentContent.id)" class="md-icon-button">
                        <thumb-down></thumb-down>
                        <v-icon icon="fa:fas fa-lock"></v-icon>
                    </md-button>
                    <md-button @click="voteDown(documentContent.id)" class="md-icon-button">
                        <v-icon icon="fa:fas fa-lock"></v-icon>
                        <bookmark></bookmark>
                    </md-button> -->
                    <!-- <div class="score-box">
                        <span class="md-headline score-text">{{ moderationScore }}</span>
                    </div> -->
                </div>
            </v-card-actions>

        </v-card>

    </div>
</template>

<script>
// import ThumbsUp from '/node_modules/vue-material-design-icons/ThumbUp.vue';
// import ThumbDown from '/node_modules/vue-material-design-icons/ThumbDown.vue';
// import Bookmark from '/node_modules/vue-material-design-icons/Bookmark.vue';
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
    max-width: 400px; //320px
    height: 300px;
    margin: 10px;
    vertical-align: top;
    flex: 1;
  }

//   .card-area {
//     height: 100%;
//   }

  .card-content {
    height: 80%;
    overflow-y: auto;
  }

.card-footer {
    display: flex;
}

.md-field {
    margin-top: -50px;
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

.v-card-actions {
    justify-content: center;
}

.keywords {
    // padding-left: 20px;
    justify-content: center;
    overflow-y: auto;
    height: 60%;
    padding-right: 20px;
}
</style>