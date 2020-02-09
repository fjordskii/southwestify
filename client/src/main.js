import Vue from 'vue';
import firebase from 'firebase/app';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import store from './store';

Vue.config.productionTip = false;
Vue.config.devtools = true;

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
}).$mount('#app');

const config = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
  authDomain: process.env.VUE_APP_AUTH_DOMAIN,
  databaseURL: process.env.VUE_APP_FIREBASE_DATABASE_URL,
  storageBucket: process.env.VUE_APP_STORAGE_BUCKET,
};

firebase.initializeApp(config);
