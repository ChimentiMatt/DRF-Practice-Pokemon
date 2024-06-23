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
  console.log(pokemonName)
  try {
    const response = await api.get('api/pokemon-count/' + pokemonName); 
    return response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
    throw error;
  }
};


export const getTrainersPokemon = async () => {
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