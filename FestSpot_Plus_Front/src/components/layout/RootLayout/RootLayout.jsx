/** @jsxImportSource @emotion/react */
import * as s from "./styles";
import React from "react";

function RootLayout({ children }) {
  return <div css={s.layout}>{children}</div>;
}

export default RootLayout;
