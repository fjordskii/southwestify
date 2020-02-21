<template>
  <v-container fill-height>
    <v-layout align-center>
      <v-flex>
        <v-card class="mx-auto text-left mb-4">
          <v-card-text>
            <p class="display-1 text--primary">
              What is Automate My Check-in?
            </p>
            <div class="text--primary">
              Automate My Check-in (aka AMC) is a web application that allows you to schedule your
              flight's check-in process up to months in advance. That way, you don't forget to do it
              the day of and get left high and dry <v-icon>mdi-airplane</v-icon>
            </div>
          </v-card-text>
        </v-card>
        <v-card class="mx-auto text-left mb-4">
          <v-card-text>
            <p class="display-1 text--primary">
              How does AMC work?
            </p>
            <div class="text--primary">
              We take your reservation, get all of the details behind the scenes, do a bunch of
              math, and then schedule a process to be ran exactly 24 hours before your scheduled
              departure time (the exact moment your check-in window opens). That's about it! Pretty
              cool, huh?
              <v-icon>mdi-airplane</v-icon>
            </div>
          </v-card-text>
        </v-card>
        <v-card class="mx-auto text-left mb-4">
          <v-card-text>
            <p class="display-1 text--primary">
              What does "beta" mean?
            </p>
            <div class="text--primary">
              Beta more or less means AMC is still a work in progress and is still in testing. If
              you find a bug, please shoot us an e-mail on our
              <a @click="navigateTo('contact')">Contact Us</a> page. That way, we can make
              everyone's experience a bit better!<v-icon>mdi-airplane</v-icon>
            </div>
          </v-card-text>
        </v-card>
        <v-card class="mx-auto text-left mb-4">
          <v-card-text>
            <p class="display-1 text--primary">
              Who created AMC? I want to shake their hand!
            </p>
            <div class="text--primary">
              Wow. You're so sweet! AMC was created by me,
              <a href="https://github.com/fjordski">fjordskii</a>. My niche is writing software that
              makes traveler's lives easier. Thanks for stopping by, hope you enjoy!
              <v-icon>mdi-airplane</v-icon>
            </div>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'FAQ',
  mixins: [UtilsMixin],
};
</script>

<style scoped></style>
