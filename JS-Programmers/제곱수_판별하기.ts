function solution(n: number) {
  let num = 1;

  while (num * num < n) {
    num += 1;

    if (num * num === n) {
      return 1;
    }
  }

  return 2;
}

console.log(solution(144));

export {};
