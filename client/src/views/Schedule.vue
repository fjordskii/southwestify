<template>
  <div class="home">
    <ScheduleCheckin></ScheduleCheckin>
  </div>
</template>

<script>
import ScheduleCheckin from '@/components/ScheduleCheckin.vue';

export default {
  name: 'Schedule',
  components: {
    ScheduleCheckin,
  },
};
</script>
