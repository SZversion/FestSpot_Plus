import React from "react";
import { Route, Routes } from "react-router-dom";
import Login from "../page/Auth/Login/Login";
import SignUp from "../page/Auth/SignUp/SignUp";

function AuthRouter(props) {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<SignUp />} />
    </Routes>
  );
}

export default AuthRouter;
