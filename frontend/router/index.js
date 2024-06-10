import { createRouter, createWebHistory } from 'vue-router';
// import Home from '@/views/Home.vue';
import Login from '../src/components/Login.vue';
import Home from '../src/components/Home.vue';
import Dashboard from '../src/components/Dashboard.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

// router.beforeEach((to, from, next) => {
//     const isAuthenticated = !!localStorage.getItem('token'); // Adjust according to your authentication logic
//     if (to.name !== 'Login' && !isAuthenticated) next({ name: 'Login' });
//     else next();
//   });

export default router;
