<template>

    <div class="executive-summary">
        <v-card
            class="mx-auto"
            variant="outlined"
            width="80%"
        >
            <v-card-item>
                <div>
                    <div class="text-h5">
                    Executive Summary
                    </div>
                    <div class="text-body-1">{{executiveSummary}}</div>
                    <div class="summary-feedback">
                            <v-btn
                                class="summary-button"
                                small
                                outlined
                                elevation="0"
                                variant="tonal"
                                icon="mdi-thumb-up">
                            </v-btn>

                            <v-btn
                                class="summary-button"
                                small
                                outlined
                                :elevation="0"
                                variant="tonal"
                                icon="mdi-thumb-down"
                                @click="expandSummaryFeedback = !expandSummaryFeedback">
                            </v-btn>
                    </div>

                    <v-expand-transition>
                    <div 
                        class="summary-feedback-text"
                        v-show="expandSummaryFeedback">
                            <v-textarea
                                outlined
                                name="summary-feedback-text"
                                label="Please enter feeback and submit..."
                                input="summaryFeedbackText"
                                ></v-textarea>
                        </div>
                    </v-expand-transition>
                </div>
            </v-card-item>
            
        </v-card>
    </div>

    <!-- <div class="mainContainer"> -->
      <!-- <div class="searchContainer">
        
        <md-field md-transparent md-clearable>
            <label>Enter your query here...</label>
            <md-input media="(prefers-color-scheme: dark)" v-model="searchString">
              <span class="md-helper-text">Helper text</span></md-input>
        </md-field>

        <div class="goButton">
          <md-button class="md-icon-button md-accent" @click="getItemsList"><chevron-right :size="45"></chevron-right></md-button>
        </div>
      </div> -->

      <!-- <div class="featuredButtons">
        <md-button class="md-accent">Bookmarked</md-button>
        <md-button class="md-accent">Trending</md-button>
        <md-button class="md-accent">Recent</md-button>
      </div> -->

            <!-- <div class="executiveSummary"> -->

                <!-- <md-content>

                    <md-card-area>
                        <md-card-header>
                        <div class="md-title">Executive Summary</div>
                        </md-card-header>

                        <md-card-content>
                        <div class="md-subhead"><span class="md-body-2">{{ executiveSummary }}</span></div>
                        </md-card-content>
                    </md-card-area>

                    <md-card-actions mt-auto>
                            <div class="score">
                                <span class="md-subheading"></span>
                            </div>
                    </md-card-actions>

                </md-content> -->

                <!-- <div class="score">
                    <span class="md-subheading"> {{ scoreSummary }}</span>
                    <span class="md-subheading summary-score-title">Score:&nbsp;</span>
                </div> -->

                <!-- <div v-if="separatorVisible">
                    <hr>
                </div> -->
            <!-- </div> -->

    <div class="list_resources">
        <div class="text-h5 text-center">
            Retrieved Documents
        </div>
        <list-cards :resources="documentList"></list-cards>
    </div>   
    <!-- </div> -->
</template>

<script>
import ListCards from '/src/components/RASIV/ListCards.vue'

export default {
  props: {
    documentList: Object,
    executiveSummary: String 
  },
  components: {
    ListCards
  },
  data() {
    return {
      separatorVisible: false,
      summaryFeedbackText: "",
      expandSummaryFeedback: false,
      scoreSummary: 15,
      resources: [{
        id: "1",
        name: "TestName1",
        summary: "TestSummary1",
        link: "www.google.com",
        keywords: ["test A", "testlong B", "testlonger C", "testlongest D", "test E", "test F"] 
      },
      {
        id: "2",
        name: "TestName2",
        summary: "We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations. Since then, millions of people have given us feedback, we’ve made several important updates and we’ve seen users find value across a range of professional use-cases, including drafting & editing content, brainstorming ideas, programming help, and learning new topics. We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations. We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations.",
        link: "www.google.com" ,
        keywords: ["test A", "testlong B", "testlonger C", "testlongest D", "test E", "test F", "test G", "test H", "testlong I", "testlonger J", "testlongest K"] 
      },
      {
        id: "3",
        name: "TestName3",
        summary: "TestSummary3",
        link: "www.google.com",
        keywords: ["test C", "test D"] 
      },
      {
        id: "4",
        name: "TestName4",
        summary: "TestSummary4",
        link: "www.google.com" 
      },
      {
        id: "5",
        name: "TestName5",
        summary: "TestSummary5",
        link: "www.google.com" 
      }]
      // resources: []
    }
  },
  computed: {
    listItems() {
      console.log("Document list updated: " + this.documentList);
      return this.documentList;
    }
  },
  methods: {
    getItemsList() {
      this.separatorVisible=true;
      console.log("searchString: " + this.searchText)
      fetch('http://127.0.0.1:8000/items?search_string=' + this.searchText)
      .then((response) => {
        if(response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        const results = [];
        let documentContent = data['documentList']
        let executiveSummary = data['searchParams']['executiveSummary']
        for (let i=0; i<documentContent.length; i++) {
          console.log("Document keywords for " + documentContent[i].name + ": ");
          console.log(documentContent[i].keywords.toString());
          results.push({
            id: documentContent[i].id.toString(),
            name: documentContent[i].name,
            summary: documentContent[i].summary,
            keywords: documentContent[i].keywords,
            link: documentContent[i].link,
            category: documentContent[i].category,
          });
        }
        console.log("Results: ");
        console.log(results);
        this.resources = results;
        this.executiveSummary = executiveSummary;
      })
      }
    }
  }
</script>

<style lang="scss" scoped>
.list_resources {
  margin: auto;
  width: 80%;
  overflow-y: auto;
  align-self: center;
  margin-top: 30px;
}

.goButton {
  padding-top: 16px;
  height: 40px;
  width: 40px;
}


.searchContainer {
  display: flex;
  padding-top: 20px;
  width: 80%;
  margin: auto;
}

.executive-summary {
    padding-bottom: 20px;
    padding-top: 20px;
    background-color: rgb(238, 238, 238);
    margin: auto;
}

:deep() .md-card {
  background-color: grey;
}

.score {
  display: flex;
  flex-direction: row-reverse;
  margin-right: 70px;
}

.summary-score-title {
  font-weight: bold;
}

.summary-feedback {
    display: flex;
    flex-direction: row-reverse;
}

.summary-button {
    background-color: rgba(255, 251, 255, 0.651)
}
</style>