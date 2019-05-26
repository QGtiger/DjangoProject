// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueRouter from 'vue-router'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import Util from './libs/util'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)//全局使用ElementUI

Vue.use(VueRouter);
Vue.use(iView);
Vue.config.productionTip = false

router.beforeEach((to, from, next)=>{
  iView.LoadingBar.start();
  let isLogin = !!localStorage.token
  console.log(isLogin)
  if (to.path === '/login' || to.path === '/register') {
    Util.title(to.meta.title);
    next()
  } else {
    Util.title(to.meta.title);
    isLogin ? next() : next('/login')
  }
})

router.afterEach((to, from, next)=>{
  iView.LoadingBar.finish();
  window.scrollTo(0,0);
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
