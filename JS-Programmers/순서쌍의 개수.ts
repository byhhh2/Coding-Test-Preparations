function solution(n: number) {
  let count = 0;

  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      count += 1;
    }
  }

  return count;
}

console.log(solution(20));

export {};
