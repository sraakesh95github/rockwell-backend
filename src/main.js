import Vue from 'vue'
import App from './App.vue'
import VueMaterial from 'vue-material'
import axios from 'axios'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.config.productionTip = false
Vue.use(VueMaterial);

axios.defaults.baseURL = 'http://127.0.0.1:8000'

new Vue({
  render: h => h(App),
}).$mount('#app')
