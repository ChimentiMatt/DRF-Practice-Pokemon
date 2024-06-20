import api from '../api';

export const getPokedex
 = async () => {
  try {
    const response = await api.get('api/pokedex/'); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};
