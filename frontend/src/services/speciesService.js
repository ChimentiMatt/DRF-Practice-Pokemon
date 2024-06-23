import api from '../api';

export const getSpecies = async () => {
  try {
    const response = await api.get('api/species/'); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};

export const getSingleSpecies = async (name) => {
  try {
    const response = await api.get('api/species/' + name); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};