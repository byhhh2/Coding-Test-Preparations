function solution(n: number, k: number) {
  return n * 12000 + k * 2000 - Math.floor(n / 10) * 2000;
}

console.log(solution(10, 3));

export {};
