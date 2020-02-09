<template>
  <div class="home">
    <v-btn color="primary" @click="navigateTo('schedule')">
      <span>Schedule Check-in</span>
    </v-btn>
  </div>
</template>

<script>
import UtilsMixin from '@/mixins/UtilsMixin.vue';

export default {
  mixins: [UtilsMixin],
};
</script>
