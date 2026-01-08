import { css } from "@emotion/react";

export const SignUpLayout = css`
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100vh;
`;

export const SignUpContainer = css`
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
  flex-direction: column;
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
  cursor: pointer;
`;

export const textFieldHelp = css`
  display: flex;
  justify-content: start;
  align-items: center;
  width: 100%;
  font-size: 1rem;
  color: red;
  margin: 0;
  margin-bottom: 2%;
`;

export const buttonContainer = css`
  width: 100%;
  margin-bottom: 1%;
  .MuiButtonBase-root {
    font-size: 1.4rem;
  }
`;

export const toLoginContainer = css`
  display: flex;
  justify-content: end;
  width: 100%;
  margin-bottom: 5%;
  font-size: 1.2rem;

  & > span {
    margin: 0 2%;
  }
`;
