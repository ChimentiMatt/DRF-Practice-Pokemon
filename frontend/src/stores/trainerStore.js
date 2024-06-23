import { defineStore } from 'pinia'

export const useTrainerStore = defineStore('trainer', {
    state: () => ({
        user: null,
        name: '',
        email: '',
        id: null
    }),
    actions: {
        setUser(userData) {
            this.user = userData;
            this.name = userData.name;
            this.email = userData.email;
            this.id = userData.id;
        },
        clearUser() {
            this.user = null;
            localStorage.removeItem('user');
        },
    },
});
