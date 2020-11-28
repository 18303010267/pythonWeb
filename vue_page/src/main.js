// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import qs from 'qs'
Vue.use(ElementUI)
Vue.use(VueResource)
Vue.config.productionTip = false
Vue.prototype.qs=qs
Vue.prototype.$axios = axios.create({
baseURL:'http://127.0.0.1:8000',
//请求前处理数据
transformRequest:[function(data){
console.log(data);
data=qs.stringify(data);
return data;
}],
//请求等待超时时间则中断
timeout: 1500,
//请求后的data处理
transformResponse: [function (data) {
console.log(data);
return data;
}]
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
