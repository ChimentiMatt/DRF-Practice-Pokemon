import api from '../api';

export const getPokemon
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('api/pokemon/', {
      headers: {
        'Authorization': `Token ${token}`
      }
    }); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};

export const getTrainersPokemon
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('api/trainers-pokemon/', {
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