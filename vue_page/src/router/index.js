import Vue from 'vue'
import Router from 'vue-router'
import home from '@/views/home'

import sliderPath from './sliderPath.js'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      meta:{
        name:'首页',
        auth:false
      },
      component: home,
      children:sliderPath
    }
  ]
})
