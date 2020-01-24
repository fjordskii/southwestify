import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;
Vue.config.devtools = true;

new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount("#app");
