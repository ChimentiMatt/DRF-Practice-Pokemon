// store.js or store.ts
import { defineStore } from 'pinia'

export const useTrainerStore = defineStore('trainer', {
    state: () => ({
        trainerObj: null,
        name: '',
    }),
    actions: {
        // increment() {
        //     this.counter++
        // },
    },
    getters: {
        // doubleCounter: (state) => state.counter * 2,
    },
})
