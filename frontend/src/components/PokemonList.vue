<template>
  <div>
    <h1>Pokemon List</h1>
    <ul>
      <li v-for="poke in pokemon" :key="poke.id">Name:{{ poke.name }}</li>
      <li v-for="poke in pokemon" :key="poke.id">Species:{{ poke.species__name }}</li>
      <li v-for="poke in pokemon" :key="poke.id">Type:{{ poke.poke_type__name }}</li>
    </ul>
  </div>
</template>

<script>

import { getTrainersPokemon } from '../services/pokemonService';

export default {
  name: 'PokemonList',
  data() {
    return{
      pokemon: [],
    }
  },
  mounted() {
    this.pokemon = this.handleCall();
  },
  methods: {
    async handleCall() {
      this.pokemon = await getTrainersPokemon();
    }
  }
};
</script>
