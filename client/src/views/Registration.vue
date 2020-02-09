<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title>Register</v-card-title>
          <v-card-text>
            <v-form v-model="isValid">
              <v-text-field
                label="Email"
                type="email"
                name="email"
                aria-autocomplete="on"
                v-model="formValues.email"
                required
                :rules="emailRules"
              ></v-text-field>
              <v-text-field
                label="password"
                name="password"
                aria-autocomplete="on"
                v-model="formValues.password"
                type="password"
                required
                :rules="passwordRules"
              ></v-text-field>
              <div v-if="showError">
                <v-alert dense outlined type="error">
                  {{ getError }}
                </v-alert>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" :disabled="!isValid" @click="postData">Register</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-btn color="primary" @click="signInWithGoogle">
          <v-icon>mdi-google</v-icon><span>&nbsp;&nbsp;Google Sign-in</span>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
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
  computed: {
    showError() {
      return this.getError !== '' && this.getStatus === 'failure';
    },
  },
  methods: {
    signInWithGoogle() {
      this.signInWithProviderRedirect();
    },
    postData(e) {
      if (this.isValid) {
        e.preventDefault();
        this.signUpWithFirebase(this.formValues.email, this.formValues.password);
      }
    },
  },
};
</script>
