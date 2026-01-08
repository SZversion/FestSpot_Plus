import api from "./axios";

export const reqSignup = async (data) => await api.post(`/api/users`, data);
