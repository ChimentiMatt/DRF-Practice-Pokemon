<template>
  <div>
    <h1>Login</h1>
    <form  @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    {{ message }}
  </div>
</template>

<script>
import { login } from '../services/authService';
import { useTrainerStore } from '../stores/trainerStore';

export default {
  data() {
    return{
      username: '', 
      password: '',
      message: '',
      trainerStore: useTrainerStore()
    }
  },
  mounted() {
  },
  methods: {
    async handleLogin() {
      login(this.username, this.password)
      .then(respons => {
        this.$router.push({ name: 'Dashboard' });
        console.log('success')
      })
      .catch(error => {
        console.log('error', error)
        this.message = error.message
      })
    },
  }
};
</script>
