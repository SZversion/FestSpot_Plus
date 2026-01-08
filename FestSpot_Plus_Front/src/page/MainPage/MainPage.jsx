/** @jsxImportSource @emotion/react */
import * as s from "./styles";
import React from "react";

function MainPage(props) {
  return (
    <div css={s.homeLayout}>
      <input type="text" placeholder="id" />
      <input type="password" placeholder="password" />
      <input type="email" placeholder="email" />
      <input type="text" placeholder="nickname" />
    </div>
  );
}

export default MainPage;
