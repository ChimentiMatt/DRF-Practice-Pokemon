<template>
  <div>
    <h1>Login</h1>
    <form  @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
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
      let attempt = await login(this.username, this.password)
      if (attempt.status === 200) this.$router.push({ name: 'Dashboard' });
      else this.message = 'Error on loggin attempt'
    },
  }
};
</script>
