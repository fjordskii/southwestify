<template>
  <v-container fill-height>
    <v-layout align-center>
      <v-flex>
        <v-title><h3 class="display-3">About</h3></v-title>
        <blockquote class="blockquote text-justify">
          Ever forget to check-in to your flight? It SUCKS! Nobody wants to get B or even the
          dreaded C seat. You're the last to board and the last to get off and often times are stuck
          sitting by the toilet.
        </blockquote>
        <blockquote class="blockquote text-justify">
          No thanks. Well, thankfully you found this site, because we're here to help! SMFC helps
          you out by allowing you to schedule your flight's check-in process. No more terrible
          seats, no more anxiety watching the clock tick down until your check-in slot opens, and no
          more button smashing trying to get 'A'. We do it all for you!
        </blockquote>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'About',
  mixins: [UtilsMixin],
};
</script>

<style scoped></style>
