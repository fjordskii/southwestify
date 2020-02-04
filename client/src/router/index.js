import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import ThankYou from '../views/ThankYou.vue';
import Login from '../views/Login.vue';
import Register from '../views/Registration.vue';
import Schedule from '../views/Schedule.vue';
import Dashboard from '../views/Dashboard.vue';
import store from '../store';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/thank-you',
    name: 'thank-you',
    component: ThankYou,
    props: true,
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
  },
  {
    path: '/schedule',
    name: 'schedule',
    component: Schedule,
    beforeEnter: (to, from, next) => {
      if (store.getters.user) {
        next();
      } else {
        next({
          name: 'home',
        });
      }
    },
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      if (store.getters.user) {
        next();
      } else {
        next({
          name: 'home',
        });
      }
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
