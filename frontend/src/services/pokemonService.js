import api from '../api';

export const getPokemon = async (pokemonName) => {
  try {
    const response = await api.get('api/pokemon/' + pokemonName); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};

export const getPokemonCaughtCount = async (pokemonName) => {
  try {
    const response = await api.get('api/pokemon/pokemon-count/' + pokemonName); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};
