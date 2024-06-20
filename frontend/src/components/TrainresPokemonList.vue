<template>
  <div>
    <h1>Trainers Pokemon</h1>
    <p v-for="poke in trainersPokemon" :key="poke.id">Name: {{ poke.name }}</p>
    <p v-for="poke in trainersPokemon" :key="poke.id">Species: {{ poke.species__name }}</p>
    <p v-for="poke in trainersPokemon" :key="poke.id">Type: {{ poke.poke_type__name }}</p>
  </div>
</template>

<script>

import { getTrainersPokemon } from '../services/pokemonService';

export default {
  name: 'PokemonList',
  data() {
    return{
      trainersPokemon: [],
    }
  },
  mounted() {
    this.pokemon = this.handleCall();
  },
  methods: {
    async handleCall() {
      this.trainersPokemon = await getTrainersPokemon();
    }
  }
};
</script>
