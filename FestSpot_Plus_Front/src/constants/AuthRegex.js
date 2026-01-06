export const JOIN_REGEX = {
  userLoginId: /^(?=.*[A-Za-z])[A-Za-z0-9]{6,20}$/,
  userPassword:
    /^(?=.*[A-Za-z])(?=.*\d)(?=.*[~!@#$%^&*()_+\-=\[\]{};':"\\|,.<>/?]).{8,20}$/,
  userNickName: /^(?=.*[가-힣A-Za-z])[가-힣A-Za-z0-9-_]{2,20}$/,
  userEmail: /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/,
  notEmpty: /^.+$/,
};

export const JOIN_REGEX_ERROR_MESSAGE = {
  userLoginId: "아이디는 영문 포함 6~20자여야 합니다.",
  userPassword: "비밀번호는 8~20자이며, 영문·숫자·특수문자를 포함해야 합니다.",
  passwordCheck: "비밀번호가 서로 일치하지 않습니다.",
  userNickName: "이름은 2~20자여야 합니다.",
  userEmail: "유효하지 않은 이메일 형식입니다.",
};
