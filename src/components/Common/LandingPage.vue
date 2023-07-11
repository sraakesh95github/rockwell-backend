<template>
      <v-toolbar
        class="toolbar-container"
        :elevation="1"
        dense
        fixed
      >

      <div class="header-logo">
        <img src="/static/rockwell_logo.png" alt="">
      </div>

      <div class="mr-auto my-2 search-container">
        <v-menu transition="scroll-y-transition">
            <template v-slot:activator="{ props }">
                <v-text-field
                hide-details
                density="compact"
                variant="outlined"
                persistent-clear
                clearable
                placeholder="Search white papers"
                append-inner-icon="mdi-magnify"
                v-model="searchString"
                v-bind="props"
                @click:append-inner="getItemsList"
                @click="getQueryHistory"
                ></v-text-field>
            </template>

            <v-list>
                <v-list-item
                v-for="query in queryHistoryList"
                :key="query"
                link
                >
                <v-list-item-title v-text="query"></v-list-item-title>
                </v-list-item>
            </v-list>

        </v-menu>
      </div>

      

      <div class="toolbar-actions">
        <v-menu transition="slide-y-transition">
        <template v-slot:activator="{ props }">
            <v-btn
                rounded
                class="ma-2"
                color="blue"
                size="x-large"
                prepend-icon="mdi-file-upload"
                variant="tonal"
                v-bind="props">File Upload
            </v-btn>
        </template>
        <!-- <div class="file-input"> -->
            <v-card
            class="mx-auto file-input"
            color="blue"
            variant="outlined">
                <v-card-item>
                    <v-file-input
                            dark
                            show-size
                            counter
                            multiple
                            label="Click Here"
                        ></v-file-input>
                </v-card-item>
            </v-card>
        <!-- </div> -->
        </v-menu>
      </div>

      <div class="text-h4 text-center text-grey">
        &nbsp; &nbsp; RASIV PORTAL &nbsp; &nbsp;
      </div>
  
        <!-- <v-btn icon>
          <v-icon>mdi-crosshairs-gps</v-icon>
        </v-btn>
  
        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn> -->

      </v-toolbar>

      <!-- <v-icon icon="fa:fas fa-lock"></v-icon> -->

      <rasiv-landing
      :documentList="resources"
      :executiveSummary="executiveSummary">
      </rasiv-landing>

  </template>
  
   <script>
  // import Menu from '/node_modules/vue-material-design-icons/Menu.vue';
  import RasivLanding from '/src/views/RasivLanding';
//   import PageFooter from '/src/components/Common/PageFooter'
import FileUpload from '/src/components/RASIV/FileUpload'
  
  export default {
      name: "LandingPage",
      data()  {
        return {
            fileUploadVisible: false,
            queryHistoryList: ['Query 1', 'Query 2'],
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
        RasivLanding,
        FileUpload
        // PageFooter
      },
      computed: {
        menuVisibility() {
          return !this.menuVisible;
        },
        fileUploadVisibility() {
            console.log("Show file upload called...")
            return this.fileUploadVisible
        }
      },
      methods: {
      getQueryHistory() {
        console.log("Query history called...")
      },
      getItemsList() {
      this.separatorVisible=true;
      console.log("searchString: " + this.searchString)
      fetch('http://127.0.0.1:8000/llm?query=' + this.searchString)
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
      },
      showFileUpload() {
        console.log("File upload: " + this.fileUploadVisible)
        this.fileUploadVisible = !this.fileUploadVisible
        return this.fileUploadVisible
      }
    }
  }
  </script>
  
  <style lang="scss" scoped>
    .file-input {
        background-color: rgb(71, 68, 68);
        min-width: 500px;
    }

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

