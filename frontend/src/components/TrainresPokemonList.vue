<template>
  <div>
    <h1>Trainers Pokemon</h1>
    <div v-for="poke in trainersPokemon">
      <p :key="poke.id">Name: {{ poke.name }}</p>
      <p :key="poke.id">Species: {{ poke.species__name }}</p>
      <p :key="poke.id">Type: {{ poke.poke_type__name }}</p> 
      --
    </div>

    <p>---</p>
  </div>
</template>

<script>

// import { getTrainersPokemon } from '../services/pokemonService';
import { getTrainerPokemon } from '../services/trainerService';

export default {
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
      this.trainersPokemon = await getTrainerPokemon();
      console.log(this.trainersPokemon)
    }
  }
};
</script>
