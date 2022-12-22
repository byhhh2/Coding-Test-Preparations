function solution(rsp: string) {
  let answer = '';

  for (const elem of rsp) {
    switch (elem) {
      case '2':
        answer += '0';
        break;

      case '0':
        answer += '5';
        break;

      case '5':
        answer += '2';
        break;
    }
  }

  return answer;
}

console.log(solution('205'));

export {};
