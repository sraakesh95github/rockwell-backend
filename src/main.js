import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import axios from 'axios'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import VueRouter from 'vue-router'

import EmailSupport from './views/EmailSupport.vue'
import RasivLanding from './views/RasivLanding.vue'
import TechSupportLanding from './views/TechSupportLanding.vue'

const router = new VueRouter({
  routes: [{
    path: '/techsupport',
    component: TechSupportLanding
  },
  {
    path: '/emailsupport',
    component: EmailSupport 
  },
  {
    path: '/rasiv',
    component: RasivLanding
  }]
});

Vue.config.productionTip = false
Vue.use(VueMaterial);
Vue.use(router);

axios.defaults.baseURL = 'http://127.0.0.1:8001'

new Vue({
  router: router,
  render: h => h(App),
}).$mount('#app')

