import Vue from 'vue';
import Vuex from 'vuex';
import firebase from 'firebase/app';
import 'firebase/auth';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: '',
    userEmail: '',
    status: '',
    error: '',
  },
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    setUserEmail(state, payload) {
      state.userEmail = payload;
    },
    removeUser(state) {
      state.user = null;
      state.userEmail = null;
    },
    setStatus(state, payload) {
      state.status = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
  },
  actions: {
    signUpAction({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('setStatus', 'loading');
        firebase
          .auth()
          .createUserWithEmailAndPassword(payload.email, payload.password)
          .then((response) => {
            commit('setUser', response.user.uid);
            commit('setUserEmail', response.user.email);
            commit('setStatus', 'success');
            commit('setError', null);
            resolve(response);
          })
          .catch((error) => {
            commit('setStatus', 'failure');
            commit('setError', error.message);
            reject(error);
          });
      });
    },
    signInAction({ commit }, payload) {
      return new Promise((resolve, reject) => {
        commit('setStatus', 'loading');
        firebase
          .auth()
          .signInWithEmailAndPassword(payload.email, payload.password)
          .then((response) => {
            commit('setUser', response.user.uid);
            commit('setUserEmail', response.user.email);
            commit('setStatus', 'success');
            commit('setError', null);
            resolve(response);
          })
          .catch((error) => {
            commit('setStatus', 'failure');
            commit('setError', error.message);
            reject(error);
          });
      });
    },
    signInWithProviderRedirect({ commit }) {
      const provider = new firebase.auth.GoogleAuthProvider();
      provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
      firebase.auth().useDeviceLanguage();

      return new Promise((resolve, reject) => {
        commit('setStatus', 'loading');
        firebase
          .auth()
          .signInWithPopup(provider)
          .then((response) => {
            console.log(response);
            commit('setUser', response.user.uid);
            commit('setUserEmail', response.user.email);
            commit('setStatus', 'success');
            commit('setError', null);
            resolve(response);
          })
          .catch((error) => {
            commit('setStatus', 'failure');
            commit('setError', error.message);
            reject(error);
          });
      });
    },
    signOutAction({ commit }) {
      firebase
        .auth()
        .signOut()
        .then(() => {
          commit('setUser', null);
          commit('setStatus', 'success');
          commit('setError', null);
        })
        .catch((error) => {
          commit('setStatus', 'failure');
          commit('setError', error.message);
        });
    },
  },
  getters: {
    status(state) {
      return state.status;
    },
    user(state) {
      return state.user;
    },
    userEmail(state) {
      return state.userEmail;
    },
    error(state) {
      return state.error;
    },
  },
  modules: {},
});
