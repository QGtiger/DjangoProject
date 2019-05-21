// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueRouter from 'vue-router'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import Util from './libs/util'

Vue.use(VueRouter);
Vue.use(iView);
Vue.config.productionTip = false

router.beforeEach((to, from, next)=>{
  iView.LoadingBar.start();
  Util.title(to.meta.title);
  next();
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
