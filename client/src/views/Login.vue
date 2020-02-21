<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title>Login</v-card-title>
          <v-card-text>
            <v-form v-model="isValid">
              <v-text-field
                label="Email"
                type="email"
                name="email"
                aria-autocomplete="on"
                v-model="formValues.email"
                required
                :rules="[v => !!v || 'Email is required']"
              ></v-text-field>
              <v-text-field
                label="password"
                v-model="formValues.password"
                name="password"
                aria-autocomplete="on"
                type="password"
                required
                :rules="[v => !!v || 'Password is required']"
              ></v-text-field>
              <div v-if="showError">
                <v-alert dense outlined type="error">
                  {{ getError }}
                </v-alert>
              </div>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" :disabled="!isValid" @click="postData">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        Haven't registered yet? <a @click="navigateTo('register')">Get started</a>.
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
    loginUrl: '/login',
    formValues: {
      email: '',
      password: '',
    },
  }),
  computed: {
    showError() {
      return this.getError !== '' && this.getStatus === 'failure';
    },
  },
  methods: {
    postData(e) {
      if (this.isValid) {
        e.preventDefault();
        this.signInWithFirebase(this.formValues.email, this.formValues.password);
      }
    },
    signInWithGoogle() {
      this.signInWithProviderRedirect();
    },
  },
};
</script>
