<template>
  <v-card class="mx-auto" style="max-width: 500px;">
    <v-toolbar color="indigo lighten-1" cards dark flat>
      <v-card-title class="title font-weight-regular">Contact Us</v-card-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <v-form ref="form" v-model="form" class="pa-4 pt-6">
      <v-text-field
        v-model="email"
        :rules="[rules.email]"
        filled
        color="deep-purple"
        label="Email address"
        type="email"
      ></v-text-field>
      <v-textarea
        v-model="body"
        auto-grow
        filled
        color="deep-purple"
        label="Body"
        rows="1"
      ></v-textarea>
      <v-checkbox v-model="agreement" :rules="[rules.required]" color="deep-purple">
        <template v-slot:label>
          I am not an airplane&nbsp; <v-icon>mdi-airplane</v-icon>
        </template>
      </v-checkbox>
    </v-form>
    <v-divider></v-divider>
    <v-card-actions>
      <v-btn text @click="$refs.form.reset()">
        Clear
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!form"
        :loading="isLoading"
        class="white--text"
        color="deep-purple accent-4"
        depressed
        >Submit</v-btn
      >
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  data: () => ({
    agreement: false,
    body:
      'Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts',
    dialog: false,
    email: undefined,
    form: false,
    isLoading: false,
    password: undefined,
    phone: undefined,
    rules: {
      email: v => (v || '').match(/@/) || 'Please enter a valid email',
      length: len => v => (v || '').length >= len || `Invalid character length, required ${len}`,
      password: v => (v || '').match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$/)
      || 'Password must contain an upper case letter, a numeric character, and a special character',
      required: v => !!v
      || 'This field is required',
    },
  }),
};
</script>
