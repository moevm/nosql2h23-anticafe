import { createRouter, createWebHistory } from 'vue-router'
import App from "@/App.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [

    { path: '/one', component: App, alias: '/'},

    {
      path: '', //'/sales/'
      name: 'main',
      component: () => import(/* webpackChunkName: "mainPage" */ '../views/MainPage.vue'),
    },

    {
      path: '/book', //'/sales/'
      name: 'book_table',
      component: () => import(/* webpackChunkName: "bookTable" */ '../views/BookTable.vue'),
    },


    {
      path: '/work', //'/sales/'
      name: 'work_table',
      component: () => import(/* webpackChunkName: "workTable" */ '../views/WorkTable.vue'),
    },

    {
      path: '/game', //'/sales/'
      name: 'game_table',
      component: () => import(/* webpackChunkName: "gameTable" */ '../views/GameTable.vue'),
    },

  ]
})

