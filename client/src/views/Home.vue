<template>
  <v-container fill-height fluid class="home">
    <v-row align="center">
      <v-col>
        <v-icon>mdi-airplanemodeactive</v-icon>
        <h1 class="display-2 flex display-4 font-weight-black">Automate My Check-in</h1>
        <p class="flex font-weight-light font-italic mb-4">
          Automate your airline's
          check-in process!
        </p>
        <v-btn large color="primary" class="mx-1" @click="getStarted">
          Get Started
          <v-icon class="ml-2">mdi-airplane</v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'Home',
  mixins: [UtilsMixin],
  methods: {
    getStarted() {
      this.navigateTo('login');
    },
  },
};
</script>

<style scoped></style>
