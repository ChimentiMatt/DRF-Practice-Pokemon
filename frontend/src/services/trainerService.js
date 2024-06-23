import api from '../api';

export const getTrainerPokemon = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('api/trainer/trainers-pokemon/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    }); 
    return response.data;
  } catch (error) {
    console.error('Error fetching pokemon:', error);
    throw error;
  }
};