<template>
  <div class="thanks">
    <v-card class="mx-auto" max-width="344" outlined>
      <v-list-item three-line>
        <v-list-item-content>
          <div class="overline mb-4">Southwest Airlines</div>
          <v-list-item-title class="headline mb-1"
            >{{ $route.query.fname }} {{ $route.query.lname }}</v-list-item-title
          >
          <v-list-item-subtitle>
            Congrats! You're scheduled with confirmation:
            {{ $route.query.conf }}</v-list-item-subtitle
          >
        </v-list-item-content>
        <v-list-item-avatar tile size="80" color="grey">
          <img src="https://media.glassdoor.com/sqll/611/southwest-airlines-squarelogo-1411584571986.png" alt="John" />
        </v-list-item-avatar>
      </v-list-item>
      <v-card-actions>
        <v-btn text>Button</v-btn>
        <v-btn text>Button</v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import UtilsMixin from '../mixins/UtilsMixin.vue';

export default {
  name: 'Thanks',
  mixins: [UtilsMixin],
  props: ['conf', 'fname', 'lname'],
  data: () => ({
    env: window.env,
    formUrl: '/schedule-flight-form',
    formValues: {
      conf: '',
      fname: '',
      lname: '',
    },
  }),
};
</script>
