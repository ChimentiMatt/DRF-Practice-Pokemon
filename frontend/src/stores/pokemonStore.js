// store.js or store.ts
import { defineStore } from 'pinia'

export const usePokemonStore = defineStore('pokemon', {
    state: () => ({
        pokemonInfo: {},
    }),
    actions: {
        setUser(pokemonInfo) {
            this.pokemonInfo = pokemonInfo;
        },
        clearPokemon() {
            this.pokemonInfo = null;
        },
    },
});
