import axios from "axios";

export const baseURL = "http://localhost:8080";

const api = axios.create({
  baseURL: baseURL,
  timeout: 10000,
});

export default api;
