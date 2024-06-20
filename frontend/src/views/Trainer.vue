<template>
    <div>
      <h1>Trainer Page</h1>
      <div v-if="trainerStore.user">
        <p>Name {{ trainerStore.name }}</p>
        <p>email: {{ trainerStore.email }}</p>
        <div v-for="item in items">{{ item.name }}</div>
      </div>

      <PokemonList />
    </div>
  </template>
  
  <script>
  import { geTrainerItems } from '../services/itemsService';
  import { useTrainerStore } from '../stores/trainerStore';
  import { getPokemon } from '../services/pokemonService'
  import PokemonList from '../components/TrainresPokemonList.vue'
  import Navbar from '../components/Navbar.vue';

  export default {
    setup() {
    },
    components: {
      PokemonList, 
      Navbar
    },
    data() {
      return{
        items: [],
        pokemon: [],
        trainerStore: useTrainerStore()
      }
    },

    mounted() {
        this.handCall()
    },
    methods: {
      async handCall() {
        // this.items = await geTrainerItems()
        this.pokemon = await getPokemon()
      },

    }
  };
  </script>
  