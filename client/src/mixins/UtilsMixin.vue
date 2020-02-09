<script>
export default {
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
    getError() {
      return this.$store.getters.error;
    },
  },
  methods: {
    navigateTo(path) {
      if (this.$route.path !== path) this.$router.push(path).catch(() => {});
    },
    signUpWithFirebase(email, password) {
      const user = {
        email,
        password,
      };
      this.$store
        .dispatch('signUpAction', user)
        .then((response) => {
          console.log(response);
          this.navigateTo('dashboard');
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
      this.$store
        .dispatch('signInAction', user)
        .then((response) => {
          console.log(response);
          this.navigateTo('dashboard');
        })
        .catch(err => this.$store.commit('setError', err));
    },
    signInWithProviderRedirect() {
      this.$store
        .dispatch('signInWithProviderRedirect')
        .then((response) => {
          console.log(response);
          this.navigateTo('dashboard');
        })
        .catch(err => this.$store.commit('setError', err));
    },
    signOutWithFirebase() {
      this.$store.dispatch('signOutAction');
      this.navigateTo('home');
    },
  },
};
</script>
