<template>
  <v-container fill-height fluid class="home">
    <v-row align="center">
      <v-col>
        <h3 class="display-3">Tired of missing your flight's check-in?</h3>
        <h2 class="mt-5 mb-5">(We can help with that)</h2>
        <v-btn large color="primary" class="mx-1" @click="navigateTo('register')">Register</v-btn>
        <v-btn large color="primary" class="mx-1" @click="navigateTo('login')">Login</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'Home',
  mixins: [UtilsMixin],
};
</script>

<style scoped>

</style>
