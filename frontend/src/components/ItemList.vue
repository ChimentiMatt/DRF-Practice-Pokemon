<template>
  <div>
    <h1>Items</h1>
    <ul>
      <li v-for="item in items" :key="item.id">{{ item.name }}</li>
    </ul>
  </div>
</template>

<script>

import { login } from '../services/authService';
import { getItems } from '../services/itemsService';

export default {
  data() {
    return{
      items: [],
    }
  },
  mounted() {
    this.items = this.handleItems();

  },
  methods: {
    async handleItems() {
      this.items = await getItems();
    }
  }
};
</script>
