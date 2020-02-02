<template>
  <v-card>
    <v-card-title>Login</v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="Email"
          v-model="formValues.email"
          required
          :rules="[v => !!v || 'Email is required']"
        ></v-text-field>
        <v-text-field
          label="password"
          v-model="formValues.password"
          type="password"
          required
          :rules="[v => !!v || 'Password is required']"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-btn color="primary" :disabled="!isValid" @click="postData">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import UtilsMixin from '@/mixins/UtilsMixin.vue';

export default {
  mixins: [UtilsMixin],
  data: () => ({
    email: '',
    password: '',
    isValid: true,
    loginUrl: '/login',
    formValues: {
      email: '',
      password: '',
    },
  }),
  methods: {
    postData(e) {
      if (this.isValid) {
        e.preventDefault();
        this.signInWithFirebase(this.formValues.email, this.formValues.password);
      }
    },
  },
};
</script>
