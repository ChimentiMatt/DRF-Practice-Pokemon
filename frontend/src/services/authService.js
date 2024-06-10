import api from '../api';
import { useTrainerStore } from '../stores/trainerStore';

export const login = async (username, password) => {
  try {
    const response = await api.post('/login/', {
      username,
      password
    });
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);
    setUser()
    return response;

  } catch (error) {
    console.error('Error logging in:', error);
    return error;
  }
};

export const setUser = async () => {
  const trainerStore = useTrainerStore()
  try {
      const response = await api.get('/auth/trainer/', {
    });
    trainerStore.trainerObj = response.data
    trainerStore.name = response.data.username
    console.log(trainerStore.trainerObj)
    return response.data;;
  } catch (error) {
    console.error(error);
  }
};
