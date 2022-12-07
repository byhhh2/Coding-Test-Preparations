function solution(n: number) {
  let num = 1;
  let answer: number[] = [];

  while (num <= n) {
    if (n % num === 0) {
      answer.push(num);
    }
    num += 1;
  }

  return answer;
}

export {};
