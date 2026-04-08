import api from "./axios";
import Cookies from "js-cookie";

export const reqSignup = async (data) =>
  await api.post(`/api/auth/signup`, data);

export const reqLogin = async (data) => {
  const token = Cookies.get("access_token") || "";
  return await api.post(
    `/api/auth/login`,
    {
      ...data,
      accessToken: token,
    },
    { withCredentials: true },
  );
};

export const reqPrincipal = async () =>
  await api.get("/api/auth/me", { withCredentials: true });
