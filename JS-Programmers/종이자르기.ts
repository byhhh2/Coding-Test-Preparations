function solution(M: number, N: number) {
  let count = 0;

  count += M - 1;
  count += M * (N - 1);

  return count;
}

export {};
