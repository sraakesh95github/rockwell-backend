<template>
    <div>
      <div class="searchContainer">
        <md-field>
            <md-input v-model="searchString"></md-input>
        </md-field>
        <md-button @click="getItemsList">GO</md-button>
      </div>

      <div id="list_resources">
        <list-cards :resources="listItems"></list-cards>
      </div>
    </div>
</template>

<script>
import ListCards from '/src/components/ListCards.vue'

export default {
  components: {
    ListCards
  },
  data() {
    return {
      searchString: '',
      resources: []
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
div.list_resources {
  margin: 0;
  width: 80%;
}

div {
  margin: auto;
  width: 80%;
}

.searchBar {
  padding-left: 0%;
  padding-right: 0%;
}

/* .goButton {

} */

.searchContainer {
  display: flex;
  padding-bottom: 50px;
}
</style>