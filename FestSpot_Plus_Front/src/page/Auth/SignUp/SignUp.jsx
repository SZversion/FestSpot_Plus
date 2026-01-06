/** @jsxImportSource @emotion/react */
import TextField from "@mui/material/TextField";
import * as s from "./styles";
import React, { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { IoEyeOffSharp, IoEyeSharp } from "react-icons/io5";
import { JOIN_REGEX } from "../../../constants/AuthRegex";

function SignUp(props) {
  const navigate = useNavigate();

  const passwordInputRef = useRef(null);

  const [buttonDisabled, setButtonDisabled] = useState(true);

  const [inputValue, setInputValue] = useState({
    userLoginId: "",
    userPassword: "",
    passwordCheck: "",
    userNickName: "",
    userEmail: "",
  });

  const [errorMessage, setErrorMessage] = useState({
    userLoginId: false,
    userPassword: false,
    passwordCheck: false,
    userNickName: false,
    userEmail: false,
  });

  const [helpText, setHelpText] = useState({
    userLoginId: "",
    userPassword: "",
    passwordCheck: "",
    userNickName: "",
    userEmail: "",
  });

  const [visible, setVisible] = useState({
    userPassword: false,
    passwordCheck: false,
  });

  const hanleInputValueOnChange = (e) => {
    setInputValue((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));

    // 빈값 검사
    if (!JOIN_REGEX["notEmpty"].test(e.target.value)) {
      setErrorMessage((prev) => ({
        ...prev,
        [e.target.name]: false,
      }));
      return;
    }

    // 비밀번호 확인 검사
    if (e.target.name === "passwordCheck") {
      setErrorMessage((prev) => ({
        ...prev,
        [e.target.name]: e.target.value !== inputValue.userPassword,
      }));
      return;
    }

    //valid 검사
    setErrorMessage((prev) => ({
      ...prev,
      [e.target.name]: !JOIN_REGEX[e.target.name].test(e.target.value),
    }));
  };

  const handleOnKeyDown = (e) => {
    if (e.keyCode === 13 && e.target.name === "email") {
      console.log("회원가입");
    }
  };

  const handlePasswordVisibleOnClick = (key) => {
    setVisible((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    // 마운트 이후에만 실행
    if (isMounted) {
      const el = passwordInputRef.current;
      if (!el) return;

      el.focus();

      // 커서를 맨 뒤로 이동
      const len = el.value.length;
      el.setSelectionRange(len, len);
    } else {
      setIsMounted(true);
    }
  }, [visible.userPassword]);

  return (
    <div css={s.SignUpLayout}>
      <div css={s.SignUpContainer}>
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
              value={inputValue.userLoginId}
              onChange={hanleInputValueOnChange}
            />
            {errorMessage.userLoginId && (
              <p css={s.textFieldHelp}>{helpText.userLoginId}</p>
            )}
          </div>
          <div css={s.textField}>
            <TextField
              inputRef={passwordInputRef}
              fullWidth={true}
              error={errorMessage.userPassword}
              type={visible.userPassword ? `text` : `password`}
              label="비밀번호를 입력하세요."
              variant="outlined"
              name="userPassword"
              value={inputValue.userPassword}
              onKeyDown={handleOnKeyDown}
              onChange={hanleInputValueOnChange}
            />
            <div
              css={s.visiblePassword}
              onClick={() => handlePasswordVisibleOnClick("userPassword")}
            >
              {visible.userPassword ? <IoEyeSharp /> : <IoEyeOffSharp />}
            </div>
            {errorMessage.userPassword && (
              <p css={s.textFieldHelp}>{helpText.userPassword}</p>
            )}
          </div>
          <div css={s.textField}>
            <TextField
              fullWidth={true}
              error={errorMessage.passwordCheck}
              type={visible.passwordCheck ? `text` : `password`}
              label="비밀번호를 다시 입력하세요."
              variant="outlined"
              name="passwordCheck"
              value={inputValue.passwordCheck}
              onChange={hanleInputValueOnChange}
              css={s.textField}
            />
            <div
              css={s.visiblePassword}
              onClick={() => handlePasswordVisibleOnClick("passwordCheck")}
            >
              {visible.passwordCheck ? <IoEyeSharp /> : <IoEyeOffSharp />}
            </div>
            {errorMessage.passwordCheck && (
              <p css={s.textFieldHelp}>{helpText.passwordCheck}</p>
            )}
          </div>
          <div css={s.textField}>
            <TextField
              fullWidth={true}
              error={errorMessage.userNickName}
              label="닉네임을 입력하세요."
              variant="outlined"
              name="userNickName"
              value={inputValue.userNickName}
              onChange={hanleInputValueOnChange}
            />
            {errorMessage.userNickName && (
              <p css={s.textFieldHelp}>{helpText.userNickName}</p>
            )}
          </div>
          <div css={s.textField}>
            <TextField
              fullWidth={true}
              error={errorMessage.userEmail}
              label="이메일을 입력하세요."
              variant="outlined"
              name="userEmail"
              value={inputValue.userEmail}
              onChange={hanleInputValueOnChange}
            />
            {errorMessage.userEmail && (
              <p css={s.textFieldHelp}>{helpText.userEmail}</p>
            )}
          </div>
        </main>
      </div>
    </div>
  );
}

export default SignUp;
