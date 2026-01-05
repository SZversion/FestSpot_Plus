import { Route, Routes } from "react-router-dom";
import UserRouter from "./UserRouter";

function RootRouter() {
  return (
    <Routes>
      <Route path="/*" element={<UserRouter />} />
    </Routes>
  );
}

export default RootRouter;
