// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import '../static/css/global.css'
import store from './store/'
import * as customfilters from './filters/filters'

Vue.config.productionTip = false

Vue.use(ElementUI);

Object.keys(customfilters).forEach(key=>{
  Vue.filter(key,customfilters[key])
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
