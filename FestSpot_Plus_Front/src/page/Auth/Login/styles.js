import { css } from "@emotion/react";

export const loginLayout = css`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
`;

export const loginContainer = css`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  width: 40rem;
  height: auto;
  padding: 3rem 4rem;
  background-color: #dbdbdb;
  border-radius: 1rem;
`;

export const header = css`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: auto;
`;

export const main = css`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: auto;
`;

export const textField = css`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  margin: 0.5rem 0;

  .MuiInputBase-input,
  .MuiInputLabel-root,
  .MuiOutlinedInput-notchedOutline {
    font-size: 1.4rem;
  }
`;

export const visiblePassword = css`
  position: absolute;
  right: 1rem;

  width: 1rem;
  height: 1rem;
  border: 1px solid red;
`;
