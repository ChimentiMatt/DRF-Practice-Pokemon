<template>
  <div>
    <h1>Pokedex</h1>

    <div v-for="poke in pokemon" :key="poke.pokedex_id">
      <p @click="handlePokemonClick(poke)" class="hover:text-red-500 hover:cursor-pointer">
        id {{ poke.pokedex_id }} {{ poke.name }}
      </p>
  </div> 

  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { getSpecies } from '../../services/speciesService'

export default {
  setup() {
    const pokemon = ref([])
    const router = useRouter()

    const handCall = async () => {
      pokemon.value = await getSpecies()
    }

    const handlePokemonClick = (poke) => {
      router.push(`/pokemon/${poke.name}`)
    }

    onMounted(() => {
      handCall()
    })

    return {
      pokemon,
      handlePokemonClick
    }
  }
}
</script>