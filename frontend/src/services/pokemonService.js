import api from '../api';

export const getPokemon
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('/pokemon/', {
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

export const geTrainerPokemon
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('/trainer-pokemon/', {
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