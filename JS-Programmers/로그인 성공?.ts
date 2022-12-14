function solution(id_pw: string[], db: string[][]) {
  let [id, pw] = id_pw;
  let currentUser = db.find(user => user.includes(id));

  if (!currentUser) {
    return 'fail';
  }

  let [, correctPw] = currentUser;

  if (correctPw === pw) {
    return 'login';
  } else {
    return 'wrong pw';
  }
}

export {};
