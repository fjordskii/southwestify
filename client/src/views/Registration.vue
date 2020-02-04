<template>
  <v-content>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="6">
          <v-card>
            <v-card-title>Register</v-card-title>
            <v-card-text>
              <v-form v-model="isValid">
                <v-text-field
                  label="Email"
                  v-model="formValues.email"
                  required
                  :rules="emailRules"
                ></v-text-field>
                <v-text-field
                  label="password"
                  v-model="formValues.password"
                  type="password"
                  required
                  :rules="passwordRules"
                ></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary" :disabled="!isValid" @click="postData">Register</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import UtilsMixin from '@/mixins/UtilsMixin.vue';

export default {
  mixins: [UtilsMixin],
  data: () => ({
    email: '',
    password: '',
    isValid: true,
    registerUrl: '/register',
    formValues: {
      email: '',
      password: '',
    },
    emailRules: [v => !!v || 'Email is required', v => /.+@.+/.test(v) || 'E-mail must be valid'],
    passwordRules: [
      v => !!v || 'Password is required',
      v => (v && v.length >= 5) || 'Password must have 5+ characters',
      v => /(?=.*[A-Z])/.test(v) || 'Must have one uppercase character',
      v => /(?=.*\d)/.test(v) || 'Must have one number',
      v => /([!@$%])/.test(v) || 'Must have one special character [!@#$%]',
    ],
  }),
  methods: {
    postData(e) {
      if (this.isValid) {
        e.preventDefault();
        this.signUpAction(this.formValues.email, this.formValues.password);
      }
    },
  },
};
</script>
