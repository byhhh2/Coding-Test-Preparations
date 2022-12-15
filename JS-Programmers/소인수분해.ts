function solution(n: number) {
  let set = new Set<number>();

  for (let num = 2; num <= n; num++) {
    while (n % num === 0) {
      n /= num;
      set.add(num);
    }
  }

  return [...set];
}

console.log(solution(420));

export {};
