import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import 'materialize-css/dist/js/materialize.min'
import Loader from '@/components/app/Loader'


Vue.config.productionTip = false

new Vue({
  store,
  router,
  vuetify,
  Loader,
  render: h => h(App)
}).$mount('#app')
