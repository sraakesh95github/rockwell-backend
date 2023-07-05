<template>
  <div class="page-container">
    <md-app md-waterfall md-mode="fixed">
        <md-app-toolbar class="md-large md-dense md-primary" id="header-container">
          <div class="navigation">
            <div class="md-toolbar-row">
              <div class="md-toolbar-section-start">
                <!-- <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
                  <Menu></Menu>
                </md-button> -->

                <span class="page-title">RASIV Portal</span>
              </div>
            </div>
            <!-- <div class="md-toolbar-row">
              <md-tabs class="md-accent" md-alignment="centered">
                <md-tab id="tab-home" md-label="RASIV" exact></md-tab>
                <md-tab id="tab-pages" md-label="Tech Support Bot"></md-tab>
                <md-tab id="tab-posts" md-label="Email"></md-tab>
              </md-tabs>
            </div> -->
          </div>
          <div class="header-logo">
            <img src="/static/rockwell_logo.png">
          </div>
        </md-app-toolbar>

        <!-- <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>RASIV</md-icon>
            <span class="md-list-item-text">RASIV</span>
          </md-list-item>

          <md-list-item>
            <md-icon>TechSupportBot</md-icon>
            <span class="md-list-item-text">TechSupportBot</span>
          </md-list-item>

          <md-list-item>
            <md-icon>EMailGenAI</md-icon>
            <span class="md-list-item-text">EmailGenAI</span>
          </md-list-item>
        </md-list>
      </md-app-drawer> -->

        <md-app-content>
        <rasiv-landing></rasiv-landing>
        </md-app-content>

        <page-footer></page-footer>
    </md-app>
  </div>
</template>

<script>
// import Menu from '/node_modules/vue-material-design-icons/Menu.vue';
import RasivLanding from '@/views/RasivLanding.vue';
import PageFooter from '/src/components/Common/PageFooter'

export default {
    name: "LandingPage",
    data()  {
      return {
        menuVisible: false
      }
    },
    components: {
      // Menu,
      RasivLanding,
      PageFooter
    },
    computed: {
      menuVisibility() {
        return !this.menuVisible;
      }
    }
}
</script>

<style lang="scss" scoped>
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
    width: 60px;
    height: 60px;
  }

  .navigation {
    width: 90%;
  }

  #header-container {
    background-color: hsl(0, 20%, 96%);
  }

  .md-title {
    font-weight: bold;
    color: #000;
  }

  // .page-container {
  //   min-height: calc(100vh - 4rem);
  // }
</style>