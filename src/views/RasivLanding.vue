<template>
    <div>
      <div class="searchContainer">
        <md-field>
            <md-input v-model="searchString"></md-input>
        </md-field>
        <md-button @click="getItemsList">GO</md-button>
      </div>

      <div class="list_resources">
        <list-cards :resources="listItems"></list-cards>
      </div>
    </div>
</template>

<script>
import ListCards from '/src/components/RASIV/ListCards.vue'

export default {
  components: {
    ListCards
  },
  data() {
    return {
      searchString: '',
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
    }
  },
  computed: {
    listItems() {
      return this.resources;
    }
  },
  methods: {
    getItemsList() {
      console.log("searchString: " + this.searchString)
      fetch('http://127.0.0.1:8000/items?search_string=' + this.searchString)
      .then((response) => {
        if(response.ok) {
          return response.json();
        }
      })
      .then((data) => {
        const results = [];
        let documentContent = data['selection']
        for (let i=0; i<documentContent.length; i++) {
          results.push({
            id: documentContent[i].id.toString(),
            name: documentContent[i].name,
            summary: documentContent[i].summary,
            ER_keywords: documentContent[i].ER_keywords,
            link: documentContent[i].link,
            category: documentContent[i].category,
          })
        }
        console.log("Results: ");
        console.log(results);
        this.resources = results;
      })
      }
    }
  }
</script>

<style scoped>
.list_resources {
  margin: auto;
  width: 80%;
}
/* 
div {
  margin: auto;
  width: 80%;
} */

.searchBar {
  padding-left: 0%;
  padding-right: 0%;
}

/* .goButton {

} */

.searchContainer {
  display: flex;
  padding-top: 50px;
  padding-bottom: 50px;
  width: 80%;
  margin: auto;
}
</style>