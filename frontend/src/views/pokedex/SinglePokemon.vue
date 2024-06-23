<template>
  <div>
    
    <h1>Pokemon Detail for {{ pokemonObject.name }}</h1>

    <p>{{ pokemonObject.name }}</p>
    <p>{{ pokemonObject.evolution }}</p>
    <p>{{ pokemonObject.pokedex_id }}</p>

    <p>Trainers who have caught: {{ pokemonCount }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getSingleSpecies } from '../../services/speciesService'
import { getPokemonCaughtCount } from '../../services/pokemonService'

export default {
  name: 'SinglePokemon',
  setup() {
    const route = useRoute();

    const pokemonObject = ref({})
    const pokemonCount = ref(0)

    const handleCall = async () => {
      pokemonObject.value = await getSingleSpecies(route.params.name)
      console.log('now', pokemonObject.value.name)
      pokemonCount.value = await getPokemonCaughtCount(pokemonObject.value.name)
      console.log(pokemonCount.value);
      // console.log('test')
    };

    onMounted(() => {
      handleCall()
    });

    return {
      pokemonObject,
      pokemonCount
    };
  },
};
</script>