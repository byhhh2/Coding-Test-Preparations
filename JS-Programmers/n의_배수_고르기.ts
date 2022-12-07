function solution(n: number, numlist: number[]) {
  let answer: number[] = [];

  for (let num of numlist) {
    if (num % n === 0) {
      answer.push(num);
    }
  }

  return answer;
}

export {};
