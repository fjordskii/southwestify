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
            <div v-if="showError">
                <v-alert dense outlined type="error">
                  {{ getError }}
                </v-alert>
              </div>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" :disabled="!isValid" @click="postData" :loading="isLoading"
            >Schedule</v-btn>
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
    loading: false,
    complete: false,
  }),
  computed: {
    showError() {
      return this.getError !== '' && this.getStatus === 'failure';
    },
    isLoading() {
      return this.loading;
    },
  },
  methods: {
    postData(e) {
      // need to pass this.userLoggedIn
      const fromValuesWithEmail = {
        ...this.formValues,
        user_email: this.getUserEmail,
      };
      e.preventDefault();
      this.loading = true;
      axios
        .post(this.formUrl, fromValuesWithEmail)
        .then(() => {
          this.complete = true;
          this.loading = false;
          this.$store.commit('setError', null);
          this.$store.commit('setStatus', null);
          this.$router.push({ path: '/thank-you', query: this.formValues });
        })
        .catch((err) => {
          this.loading = false;
          this.$store.commit('setError', err);
          this.$store.commit('setStatus', 'failure');
        });
    },
  },
};
</script>
