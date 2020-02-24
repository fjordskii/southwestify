<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app>
      <v-list dense>
        <v-list-item v-if="userLoggedIn">
          <v-list-item-content>
            <v-list-item-title>{{ getUserEmail }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="homeNavigation">
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('login')" v-if="!userLoggedIn">
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('register')" v-if="!userLoggedIn">
          <v-list-item-action>
            <v-icon>mdi-account-check</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('about')">
          <v-list-item-action>
            <v-icon>mdi-alert-circle-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>About</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('FAQ')">
          <v-list-item-action>
            <v-icon>mdi-comment-question-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>FAQ</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('schedule')" v-if="userLoggedIn">
          <v-list-item-action>
            <v-icon>mdi-calendar-today</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Schedule</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="signOutWithFirebase" v-if="userLoggedIn">
          <v-list-item-action>
            <v-icon>mdi-account-box</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="navigateTo('contact')">
          <v-list-item-action>
            <v-icon>mdi-email-outline</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact Us</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app color="indigo" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Automate My Check-in (beta)</v-toolbar-title>
    </v-app-bar>

    <v-content>
      <v-container class="fill-height" fluid>
        <div align="center" justify="center" :class="{'row': !$vuetify.breakpoint.xs}">
          <v-col class="text-center">
            <router-view></router-view>
          </v-col>
        </div>
      </v-container>
    </v-content>
    <!-- <v-footer color="indigo" app>
      <span class="white--text">&copy; 2020</span>
    </v-footer> -->
  </v-app>
</template>

<script>
import UtilsMixin from '@/mixins/UtilsMixin.vue';

export default {
  name: 'App',
  mixins: [UtilsMixin],
  data: () => ({
    drawer: null,
  }),
  methods: {
    homeNavigation() {
      if (this.userLoggedIn) {
        return this.navigateTo('dashboard');
      }
      return this.navigateTo('/');
    },
  },
  props: {
    source: String,
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}
</style>
