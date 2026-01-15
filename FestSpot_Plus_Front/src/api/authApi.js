import api from "./axios";

export const reqSignup = async (data) =>
  await api.post(`/api/users/signup`, data);

export const reqLogin = async (data) =>
  await api.post(`/api/users/login`, data);
