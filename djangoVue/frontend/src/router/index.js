import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/account/Login'
import Register from '@/components/account/register'
import Collapse from '@/components/collapse'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      meta: {
        title: '首页'
      },
      component: Collapse
    },
    {
      path: '/login',
      meta: {
        title: '登录'
      },
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      meta: {
        title: '注册'
      },
      name: 'register',
      component: Register
    }
  ]
})
