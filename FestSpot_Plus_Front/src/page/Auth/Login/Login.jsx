/** @jsxImportSource @emotion/react */
import * as s from "./styles";
import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import { IoEyeSharp, IoEyeOffSharp } from "react-icons/io5";

function Login(props) {
  const [errorMessage, setErrorMessage] = useState({
    userLoginId: false,
    userPassword: false,
  });

  const [visible, setVisible] = useState({
    userPassword: false,
  });

  const handlePasswordVisibleOnClick = (key) => {
    setVisible((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  useState(() => {
    console.log(visible);
  }, [visible]);

  return (
    <div css={s.loginLayout}>
      <div css={s.loginContainer}>
        <header css={s.header}>
          <div>logo</div>
        </header>
        <main css={s.main}>
          <div css={s.textField}>
            <TextField
              fullWidth={true}
              error={errorMessage.userLoginId}
              label="아이디를 입력하세요."
              variant="outlined"
              name="userLoginId"
            />
          </div>
          <div css={s.textField}>
            <TextField
              fullWidth={true}
              error={errorMessage.userPassword}
              //   type={visible.userPassword ? `text` : `password`}
              label="비밀번호를 입력하세요."
              variant="outlined"
              name="userPassword"
            />
            <div
              css={s.visiblePassword}
              onClick={() => handlePasswordVisibleOnClick("userPassword")}
            >
              {/* {visible.userPassword ? <IoEyeSharp /> : <IoEyeOffSharp />} */}
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

export default Login;
