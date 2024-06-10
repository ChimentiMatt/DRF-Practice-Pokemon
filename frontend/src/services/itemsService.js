import api from '../api';

export const getItems
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('/items/', {
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

export const geTrainerItems
 = async () => {
  let token = localStorage.getItem('token')
  try {
    const response = await api.get('/trainer-items/', {
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
