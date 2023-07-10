<template>
      <v-toolbar
        class="toolbar-container"
        :elevation="1"
        dense
        floating
      >

      <div class="header-logo">
        <img src="/static/rockwell_logo.png" alt="">
      </div>

      <div class="mr-auto my-2 search-container">
        <v-text-field
          hide-details
          density="compact"
          variant="outlined"
          persistent-clear
          clearable
          placeholder="Search white papers"
          append-inner-icon="mdi-magnify"
          v-model="searchString"
          @click:append-inner="getItemsList"
        ></v-text-field>
      </div>
  
        <!-- <v-btn icon>
          <v-icon>mdi-crosshairs-gps</v-icon>
        </v-btn>
  
        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn> -->

      </v-toolbar>

      <v-icon icon="fa:fas fa-lock"></v-icon>

      <rasiv-landing
      :documentList="resources"
      :executiveSummary="executiveSummary"></rasiv-landing>

  </template>
  
   <script>
  // import Menu from '/node_modules/vue-material-design-icons/Menu.vue';
  import RasivLanding from '/src/views/RasivLanding';
//   import PageFooter from '/src/components/Common/PageFooter'
  
  export default {
      name: "LandingPage",
      data()  {
        return {
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
            }],
            executiveSummary: 'Watson is an artificial intelligence platform developed by IBM. It leverages various AI technologies, including natural language processing, machine learning, and data analytics, to provide a wide range of cognitive computing capabilities. The Watson platform offers a suite of services and tools that enable businesses and developers to harness the power of AI in diverse applications. It can process and analyze large volumes of structured and unstructured data, including text, images, and audio, to extract valuable insights and make informed decisions. One of the notable features of Watson is its natural language understanding and processing capabilities. It can comprehend and interpret human language, allowing for advanced language-based interactions and applications. Watson can perform tasks such as language translation, sentiment analysis, speech recognition, and language generation.',
          menuVisible: false,
          searchString: ''
        }
      },
      components: {
        // Menu,
        RasivLanding
        // PageFooter
      },
      computed: {
        menuVisibility() {
          return !this.menuVisible;
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

    .search-container {
        width: 50%;
    }

    .toolbar-container {
        background-color:lightgrey;
    }

    .md-app {
      max-height: 925px;
      border: 1px solid rgba(#000, .12);
    }
  
    .tab-group {
      background-color: #000;
    }
  
    // /deep/ .md-ripple {
    //   background-color: #000;
    // }
     // Demo purposes only
    .md-drawer {
      width: 230px;
      max-width: calc(100vw - 125px);
    }
  
    .page-title {
      padding-left: 20px; 
      font-size: 2.5rem;
      color: rgb(152, 50, 50);
    }

    .header-logo {
      display: flex;
      width: 40px;
      height: 40px;
      margin: 30px;
    }
  
    .navigation {
      width: 90%;
    }
  
    #header-container {
      background-color: hsl(0, 20%, 96%);
    }
    
    .toolbar-container {
        background-color: rgb(254, 254, 254);
    }

    .md-title {
      font-weight: bold;
      color: #000;
    }
  
    // .page-container {
    //   min-height: calc(100vh - 4rem);
    // }
  </style>

