<template>
  <div class="home">
    <Confirmation/>
  </div>
</template>

<script>
// @ is an alias to /src
import Confirmation from '@/components/Confirmation.vue';

export default {
  name: 'home',
  components: {
    Confirmation,
  },
};
</script>
