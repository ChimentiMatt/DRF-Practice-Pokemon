import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from '../router';
import axios from 'axios'
import './style.css'
import App from './App.vue'
import { useTrainerStore } from './stores/trainerStore';

const app = createApp(App)

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const pinia = createPinia()
app.use(pinia)


app.mixin({
    beforeMount(){
        const trainerStore = useTrainerStore();
        const savedTrainer = localStorage.getItem('trainer');
        if (savedTrainer) trainerStore.setUser(JSON.parse(savedTrainer))
    }
})

app.use(router);
app.mount('#app');
