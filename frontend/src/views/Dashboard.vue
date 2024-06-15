<template>
    <div>
      <h1>dashboard</h1>
      <div v-if="trainerStore.trainerObj">
        <p>Welcome {{ trainerStore.name }}</p>
        <div v-for="item in items">{{ item.name }}</div>
      </div>

      <PokemonList />
    </div>
  </template>
  
  <script>
  import { geTrainerItems } from '../services/itemsService';
  import { useTrainerStore } from '../stores/trainerStore';
  import { getPokemon } from '../services/pokemonService'
  import PokemonList from '../components/PokemonList.vue'

  export default {
    setup() {
    },
    components: {
      PokemonList
    },
    data() {
      return{
        items: [],
        pokemon: [],
        trainerStore: useTrainerStore()
      }
    },

    mounted() {
        console.log(this.trainerStore)
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
  