<template>
  <div>
    
    <h1>Pokemon Detail for {{ pokemonObject.name }}</h1>

    <p>{{ pokemonObject.name }}</p>
    <p>{{ pokemonObject.evolution }}</p>
    <p>{{ pokemonObject.pokedex_id }}</p>

    <h1>TODO Display how many trainers have this pokemon</h1>
    <p>Number of trainers who caught: NA</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getSingleSpecies } from '../../services/speciesService'

export default {
  name: 'SinglePokemon',
  setup() {
    const route = useRoute();

    const pokemonName = ref('')
    const pokemonObject = ref({})

    const handleCall = async () => {
      pokemonObject.value = await getSingleSpecies(route.params.name)
      console.log(pokemonObject.value);
      console.log('test')
    };

    onMounted(() => {
      handleCall()
    });

    return {
      pokemonObject,
    };
  },
};
</script>