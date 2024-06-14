import { createRouter, createWebHistory } from 'vue-router';
// import Home from '@/views/Home.vue';
import Login from '../src/views/Login.vue';
import SignUp from '../src/views/SignUp.vue';
import Home from '../src/views/Home.vue';
import Dashboard from '../src/views/Dashboard.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

export default router;
