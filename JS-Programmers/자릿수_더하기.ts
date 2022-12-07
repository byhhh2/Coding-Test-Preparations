function solution(n: number) {
  let tmp = n;
  let answer = 0;

  while (tmp > 0) {
    answer += tmp % 10;
    tmp = Math.floor(tmp / 10);
  }

  return answer;
}

console.log(solution(930211));

export {};
