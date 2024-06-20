<template>
  <div>
    <h1>Pokedex</h1>
      <div v-for="poke in pokemon">id {{ poke.pokedex_id}} {{ poke.name }} </div>
  </div>
</template>

<script>
import { getPokedex } from '../services/pokedexService'


export default {
  setup() {
  },
  components: {
  },
  data() {
    return{
      pokemon: [],
    }
  },

  mounted() {
      this.handCall()
  },
  methods: {
    async handCall() {
      // this.items = await geTrainerItems()
      this.pokemon = await getPokedex()
    },

  }
};
</script>
