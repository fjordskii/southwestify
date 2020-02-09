<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card-title>Schedule Check-in</v-card-title>
        <v-card-text>
          <v-form v-model="isValid">
            <v-text-field
              label="Confirmation #"
              v-model="formValues.conf"
              :rules="[v => !!v || 'Confirmation is required']"
            ></v-text-field>
            <v-text-field
              label="First Name"
              v-model="formValues.fname"
              :rules="[v => !!v || 'First Name is required']"
            ></v-text-field>
            <v-text-field
              label="Last Name"
              v-model="formValues.lname"
              :rules="[v => !!v || 'Last Name is required']"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" :disabled="!isValid" @click="postData">Schedule</v-btn>
        </v-card-actions>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'ScheduleCheckin',
  mixins: [UtilsMixin],
  data: () => ({
    isValid: true,
    env: window.env,
    formUrl: '/schedule-flight-form',
    formValues: {
      conf: '',
      fname: '',
      lname: '',
    },
    complete: false,
  }),
  methods: {
    postData(e) {
      e.preventDefault();
      axios
        .post(this.formUrl, this.formValues)
        .then(() => {
          this.complete = true;
          this.$router.push({ path: '/thank-you', query: this.formValues });
        })
        .catch(err => console.log(err));
    },
  },
};
</script>
