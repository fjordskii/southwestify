<template>
  <div class="hello">
    <v-form>
      <v-container>
        <v-row>
          <v-col cols="12" sm="12" md="3">
            <v-text-field label="Confirmation #" filled v-model="formValues.conf"></v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="3">
            <v-text-field label="First Name" filled v-model="formValues.fname"></v-text-field>
          </v-col>
          <v-col cols="12" sm="12" md="3">
            <v-text-field label="Last Name" filled v-model="formValues.lname"></v-text-field>
          </v-col>
        </v-row>
        <div class="my-4">
          <v-btn depressed small color="primary" @click="postData">Schedule Check-in</v-btn>
        </div>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import axios from "axios";
import UtilsMixin from "../mixins/UtilsMixin.vue";

export default {
  name: "Confirmation",
  mixins: [UtilsMixin],
  data: () => ({
    env: window.env,
    formUrl: "/schedule-flight-form",
    formValues: {
      conf: "",
      fname: "",
      lname: "",
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
          this.$router.push({ path: "/thank-you", query: this.formValues });
        })
        .catch(err => console.log(err));
    },
  },
};
</script>
