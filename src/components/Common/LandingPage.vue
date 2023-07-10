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
          prepend-icon="mdi-magnify"
          persistent-clear
          clearable
          placeholder="Search white papers"
        ></v-text-field>
      </div>
  
        <v-btn icon>
          <v-icon>mdi-crosshairs-gps</v-icon>
        </v-btn>
  
        <v-btn icon>
          <v-icon>mdi-dots-vertical</v-icon>
        </v-btn>
      </v-toolbar>

      <v-icon icon="fa:fas fa-lock"></v-icon>

      <rasiv-landing></rasiv-landing>

  </template>
  
  <script>
  // import Menu from '/node_modules/vue-material-design-icons/Menu.vue';
  import RasivLanding from '/src/views/RasivLanding';
//   import PageFooter from '/src/components/Common/PageFooter'
  
  export default {
      name: "LandingPage",
      data()  {
        return {
          menuVisible: false
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

