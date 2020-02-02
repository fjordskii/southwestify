<script>
export default {
  STATUS_SUCCESS: 'success',
  STATUS_FAILURE: 'failure',
  STATUS_LOADING: 'loading',
  computed: {
    environment() {
      return window.env;
    },
    userLoggedIn() {
      return this.$store.getters.user;
    },
    getStatus() {
      return this.$store.getters.status;
    },
  },
  methods: {
    signUpWithFirebase(email, password) {
      const user = {
        email,
        password,
      };
      this.$store.dispatch('signUpAction', user)
        .then((response) => {
          console.log(response);
          this.$router.push({ path: '/dashboard' });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    signInWithFirebase(email, password) {
      const user = {
        email,
        password,
      };
      this.$store.dispatch('signInAction', user)
        .then((response) => {
          console.log(response);
          this.$router.push({ path: '/dashboard' });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    signOutWithFirebase() {
      this.$store.dispatch('signOutAction');
      this.$router.push({ path: '/' });
    },
  },
};
</script>
