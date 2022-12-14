function solution(n: number) {
  let num = 1;

  for (let index = 1; index < n; index++) {
    num += 1;
    while (String(num).includes('3') || num % 3 === 0) {
      num += 1;
    }
  }

  return num;
}

console.log(solution(15));

export {};
