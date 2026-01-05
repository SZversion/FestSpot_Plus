import React from "react";
import { Route, Routes } from "react-router-dom";
import Login from "../page/Auth/Login/Login";

function AuthRouter(props) {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
    </Routes>
  );
}

export default AuthRouter;
