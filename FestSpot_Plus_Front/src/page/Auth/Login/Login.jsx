/** @jsxImportSource @emotion/react */
import * as s from "./styles";
import React, { useEffect, useRef, useState } from "react";
import TextField from "@mui/material/TextField";
import { IoEyeSharp, IoEyeOffSharp } from "react-icons/io5";
import {
  JOIN_REGEX,
  JOIN_REGEX_ERROR_MESSAGE,
} from "../../../constants/AuthRegex";
import Swal from "sweetalert2";
import Cookies from "js-cookie";
import Button from "@mui/material/Button";
import { Link, useNavigate } from "react-router-dom";
import { reqLogin } from "../../../api/authApi";
import { useQueryClient } from "@tanstack/react-query";
import usePrincipalQuery from "../../../queries/auth/usePrincipalQuery";

function Login(props) {
  const passwordInputRef = useRef(null);
  const principalQuery = usePrincipalQuery();
  const principal = principalQuery?.data?.data || [];
  const queryClient = useQueryClient();
  const navigate = useNavigate();
  const [buttonDisabled, setButtonDisabled] = useState(true);

  const [inputValue, setInputValue] = useState({
    userLoginId: "",
    userPassword: "",
  });

  const [errorMessage, setErrorMessage] = useState({
    userLoginId: false,
    userPassword: false,
  });

  const [helpText, setHelpText] = useState({
    userLoginId: "",
    userPassword: "",
  });

  const [visible, setVisible] = useState({
    userPassword: false,
  });

  useEffect(() => {
    const isEmptyValue = !!Object.values(inputValue).filter(
      (value) => !value.trim(),
    ).length;
    const isError = !!Object.values(errorMessage).filter((value) => !!value)
      .length;
    setButtonDisabled(isEmptyValue || isError);

    const errorEntries = Object.entries(errorMessage);
    errorEntries.forEach(([key, value]) => {
      setHelpText((prev) => ({
        ...prev,
        [key]: !value ? "" : JOIN_REGEX_ERROR_MESSAGE[key],
      }));
    });
  }, [errorMessage]);

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

    //valid 검사
    setErrorMessage((prev) => ({
      ...prev,
      [e.target.name]: !JOIN_REGEX[e.target.name].test(e.target.value),
    }));
  };

  const handleOnKeyDown = (e) => {
    if (e.keyCode === 13 && e.target.name === "userPassword") {
      handleLoginOnClick();
    }
  };

  const handleLoginOnClick = async (e) => {
    try {
      const response = await reqLogin(inputValue);
      const userNickname = response?.data.userNickname;

      await queryClient.invalidateQueries({
        queryKey: ["principal"],
      });

      // 탈퇴한 회원정보로 로그인하면 막음
      if (!!principal?.deletedAt) {
        Cookies.remove("access_token");
        await queryClient.invalidateQueries({
          queryKey: ["principal"],
        });
        await Swal.fire({
          title: "탈퇴한 회원입니다.",
          icon: "error",
        });
        return;
      }

      await Swal.fire({
        title: "로그인 성공",
        text: `${userNickname}님 환영합니다.`,
        icon: "success",
        showConfirmButton: false,
        timer: 1500,
        timerProgressBar: true,
      });

      // navigate("/");
    } catch (error) {
      await Swal.fire({
        title: "로그인 실패",
        html: `${error.response?.data?.detail}`,
        icon: "error",
      });
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
          <div css={s.buttonContainer}>
            <Button
              fullWidth={true}
              disabled={buttonDisabled}
              variant="contained"
              onClick={handleLoginOnClick}
            >
              로그인
            </Button>
          </div>
          <div css={s.toSignUpContainer}>
            <span>계정이 없으신가요?</span>
            <Link to={"/auth/signup"}>회원가입</Link>
          </div>
        </main>
      </div>
    </div>
  );
}

export default Login;
