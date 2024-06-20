<template>
  <div class="flex justify-center items-center bg-slate-500 h-[3rem]">
    <div class="flex gap-4">
      <router-link 
        to="/trainer" 
        class="text-white" 
        :class="{'font-bold border-b-2 border-white': isActive('/trainer')}"
        >
        Trainer
      </router-link>
      <router-link 
        to="/pokedex" 
        class="text-white" 
        :class="{'font-bold border-b-2 border-red': isActive('/pokedex')}"
        >
        Pokedex
      </router-link>
    </div>
  </div>
</template>

<script>
import { useRoute } from 'vue-router'

export default {
    // name: 'Navbar',
  setup() {
    const route = useRoute()

    const isActive = (path) => {
      return route.path === path
    }

    return { isActive }
  },
  data() {
    return{
    }
  },
  mounted() {
  },
  methods: {
  }
};
</script>
