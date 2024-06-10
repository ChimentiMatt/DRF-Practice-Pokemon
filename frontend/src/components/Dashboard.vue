<template>
    <div>
      <div v-if="trainerStore.trainerObj">
        <p>Welcome {{ trainerStore.name }}</p>

        <div v-for="item in items">{{ item.name }}</div>
      </div>
    </div>
  </template>
  
  <script>
  import { getItems, geTrainerItems } from '../services/itemsService';
  import { useTrainerStore } from '../stores/trainerStore';
  
  export default {
    data() {
      return{
        items: [],
        trainerStore: useTrainerStore()
      }
    },
    mounted() {
        console.log(this.trainerStore)
        this.handleGetItems()
    },
    methods: {
      async handleGetItems() {
        this.items = await geTrainerItems()
      },

    }
  };
  </script>
  