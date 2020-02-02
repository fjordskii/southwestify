<template>
  <v-jumbotron color="grey lighten-2">
    <v-container fill-height>
      <v-layout align-center>
        <v-flex>
          <h3 class="display-3">Welcome to Schedule My Flight Check-in!</h3>
                    <v-divider class="my-3"></v-divider>
          <blockquote class="blockquote text-justify">
            Ever forget to check-in to your flight? It SUCKS! Nobody wants to get high B or even the
            dreaded C seat. You're the last to board and the last to get off and often times are
            stuck sitting by the toilet.
          </blockquote>
          <blockquote class="blockquote text-justify">
            No thanks. Well, thankfully you found this site, because we're here to help! SMFC helps
            you out by allowing to schedule your flight's check-in process. No more terrible seats,
            no more anxiety watching the clock tick down until your check-in slot opens, and no more
            button smashing trying to get 'A'. We do it all for you!
          </blockquote>
          <v-divider class="my-3"></v-divider>
          <div class="title mb-3">Start Scheduling Flights Now!</div>
          <v-btn large color="primary" class="mx-0">Get Started</v-btn>
        </v-flex>
      </v-layout>
    </v-container>
  </v-jumbotron>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped></style>
