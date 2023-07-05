<template>
    <div class="mainContainer">
      <div class="searchContainer">
        <md-field md-transparent md-clearable>
            <label>Enter your query here...</label>
            <md-input media="(prefers-color-scheme: dark)" v-model="searchString">
              <span class="md-helper-text">Helper text</span></md-input>
        </md-field>
        <div class="goButton">
          <md-button class="md-icon-button md-accent" @click="getItemsList"><chevron-right :size="45"></chevron-right></md-button>
        </div>
      </div>

      <div class="featuredButtons">
        <md-button class="md-accent">Bookmarked</md-button>
        <md-button class="md-accent">Trending</md-button>
        <md-button class="md-accent">Recent</md-button>
      </div>

      <div class="executiveSummary">
        <md-content>
          <md-card-area>
            <!-- <md-card-header>
              <div class="md-title">Executive Summary</div>
            </md-card-header> -->

            <md-card-content>
              <div class="md-subhead"><span class="md-body-2">{{ executiveSummary }}</span></div>
            </md-card-content>
          </md-card-area>

          <!-- <md-card-actions mt-auto>
                <div class="score">
                    <span class="md-subheading"></span>
                </div>
            </md-card-actions> -->

        </md-content>
        <!-- <div class="score" v-if="separatorVisible"> -->
          <div class="score">
          <span class="md-subheading"> {{ scoreSummary }}</span>
            <span class="md-subheading summary-score-title">Score:&nbsp;</span>
        </div>
        <!-- <div v-if="separatorVisible"> -->
        <div>
          <hr>
        </div>
      </div>

      <div class="list_resources">
        <list-cards :resources="listItems"></list-cards>
      </div>
    </div>
</template>

<script>
import ListCards from '/src/components/RASIV/ListCards.vue'
import ChevronRight from '/node_modules/vue-material-design-icons/ChevronRight.vue';

export default {
  components: {
    ListCards,
    ChevronRight
  },
  data() {
    return {
      searchString: '',
      executiveSummary: 'Watson is an artificial intelligence platform developed by IBM. It leverages various AI technologies, including natural language processing, machine learning, and data analytics, to provide a wide range of cognitive computing capabilities. The Watson platform offers a suite of services and tools that enable businesses and developers to harness the power of AI in diverse applications. It can process and analyze large volumes of structured and unstructured data, including text, images, and audio, to extract valuable insights and make informed decisions. One of the notable features of Watson is its natural language understanding and processing capabilities. It can comprehend and interpret human language, allowing for advanced language-based interactions and applications. Watson can perform tasks such as language translation, sentiment analysis, speech recognition, and language generation.',
      separatorVisible: false,
      scoreSummary: 15,
      resources: [{
        id: "1",
        name: "TestName1",
        summary: "TestSummary1",
        link: "www.google.com" 
      },
      {
        id: "2",
        name: "TestName2",
        summary: "We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations. Since then, millions of people have given us feedback, we’ve made several important updates and we’ve seen users find value across a range of professional use-cases, including drafting & editing content, brainstorming ideas, programming help, and learning new topics. We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations. We launched ChatGPT as a research preview so we could learn more about the system’s strengths and weaknesses and gather user feedback to help us improve upon its limitations.",
        link: "www.google.com" 
      },
      {
        id: "3",
        name: "TestName3",
        summary: "TestSummary3",
        link: "www.google.com" 
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
      return this.resources;
    }
  },
  methods: {
    getItemsList() {
      this.separatorVisible=true;
      console.log("searchString: " + this.searchString)
      fetch('http://127.0.0.1:8000/items?search_string=' + this.searchString)
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
}

.goButton {
  padding-top: 16px;
  height: 40px;
  width: 40px;
}

.mainContainer {
  width: 80%;
  margin: auto;
  align-self: center;
}

.searchContainer {
  display: flex;
  padding-top: 20px;
  // padding-bottom: 30px;
  width: 80%;
  margin: auto;
}

.executiveSummary {
  padding-bottom: 30px;
}

/deep/ .md-card {
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
</style>