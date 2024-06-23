import { createRouter, createWebHistory } from 'vue-router';
// import Home from '@/views/Home.vue';
import Login from '../src/views/Login.vue';
import SignUp from '../src/views/SignUp.vue';
import Home from '../src/views/Home.vue';
import Trainer from '../src/views/Trainer.vue';
import Pokedex from '../src/views/pokedex/Pokedex.vue';
import SinglePokemon from '../src/views/pokedex/SinglePokemon.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login },
  { path: '/trainer', name: 'Trainer', component: Trainer },
  { path: '/pokedex', name: 'Pokedex', component: Pokedex },
  { path: '/pokemon/:name', name: 'SinglePokemon', component: SinglePokemon }
];

const router = createRouter({
  history: createWebHistory(''),
  routes,
});

export default router;
