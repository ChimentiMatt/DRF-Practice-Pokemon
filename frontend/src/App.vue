<script setup>
import UserList from './components/UserList.vue'
import ItemList from './components/ItemList.vue'
import Login from './components/Login.vue'
</script>

<template>
  <!-- <Login /> -->
  <RouterView />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
