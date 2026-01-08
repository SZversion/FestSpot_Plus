import React from "react";
import MainLayout from "../components/layout/MainLayout/MainLayout";
import { Route, Routes } from "react-router-dom";
import MainPage from "../page/MainPage/MainPage";
import AuthRouter from "./AuthRouter";

function UserRouter(props) {
  return (
    <MainLayout>
      <Routes>
        <Route path="/auth/*" element={<AuthRouter />} />
        <Route path="/" element={<MainPage />} />
      </Routes>
    </MainLayout>
  );
}

export default UserRouter;
