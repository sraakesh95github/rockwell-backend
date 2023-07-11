<template>
    <div>

        <v-card 
        width="1400" 
        variant="tonal"
        class="card-box"
        color="dark"
        elevation="1">

            <div class="main-content-area">

                <v-card-item 
                    class="card-area"
                    @click="documentLink(documentContent)">

                        <v-card-title>
                            <div 
                            class="text-decoration-underline"
                            >{{documentContent.name}}</div>
                        </v-card-title>

                </v-card-item>
                        <!-- <v-card-text
                        class="card-content">
                            <div @click="documentLink(documentContent)" class="md-subheading">
                            {{documentContent.summary}}
                            </div>
                        </v-card-text> -->
                        
                <div 
                class="pages">
                    <v-btn
                    class="mx-1 my-1 text-decoration-underline"
                    variant="tonal" 
                    color="blue"
                    v-for="keyword in documentContent.keywords"
                    rounded="xl"
                    :key="keyword">{{ keyword }}</v-btn>
                </div>

                <div 
                class="keywords mx-3 my-2">
                    <div
                    class="text-uppercase font-weight-bold">
                        Keywords: &nbsp; 
                    </div>
                    <div
                    variant="plain" 
                    v-for="keyword in documentContent.keywords"
                    :key="keyword">{{ keyword }}, &nbsp;</div>
                </div>
        
            </div>

            <div class="action-area">
                    <div class="card-footer">

                        <v-btn
                        class="ma-2"
                        :elevation="0"
                        icon="mdi-heart"></v-btn>


                        <v-btn
                        class="ma-2"
                        :elevation="0"
                        icon="mdi-bookmark"></v-btn>
                        
                    </div>
            </div>

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

.main-content-area {
    width: 1100px;
}

  .card-box {
    padding: 7px;
    max-width: 1100px; //320px
    margin: 10px;
    display: inline-flex;
  }

  .action-area {
    width: 60px;
  }


//   .card-content {
//     height: 80%;
//     overflow-y: auto;
//   }


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

.keywords {
//     // padding-left: 20px;
//     justify-content: center;
//     overflow-y: auto;
//     height: 60%;
//     padding-right: 20px;
display: inline-flex;
margin-top: 10px;
margin-bottom: 5px
}

.pages {
    margin-top: 10px;
    margin-bottom: 5px;
}

.card-footer {
    width: 50px;
}
</style>