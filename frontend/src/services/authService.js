import api from '../api';
import { useTrainerStore } from '../stores/trainerStore';

export const login = async (username, password) => {
  const response = await api.post('/accounts/login/', {
    email: username,
    password
  });
  localStorage.setItem('access_token', response.data.access);
  localStorage.setItem('refresh_token', response.data.refresh);
  setUser();
  return response;
};

export const setUser = async () => {
  const trainerStore = useTrainerStore()
  try {
      const response = await api.get('/api/trainer-details/', {
    });
    localStorage.setItem('trainer', JSON.stringify(response.data));
    trainerStore.setUser(response.data);
    return response.data;;

  } catch (error) {
    console.error(error);
  }
};