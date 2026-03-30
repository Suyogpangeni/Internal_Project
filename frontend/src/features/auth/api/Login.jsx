import axios from "axios";

// API base constant
const api_base = import.meta.env.VITE_API_BASE || "http://localhost:8000";

// Register User
export const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${api_base}/Authentication/RegisterUser`, userData);
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
};

// Login User
export const loginUser = async (loginData) => {
  try {
    const response = await axios.post(`${api_base}/Authentication/LoginUser`, loginData);
    return response.data;
  } catch (error) {
    throw error.response?.data || error;
  }
};
