function solution(n: number) {
  let sum = 0;

  for (let num = 2; num <= n; num += 2) {
    sum += num;
  }

  return sum;
}
