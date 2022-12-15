function solution(n: number) {
  let count = 0;

  for (let num = 4; num <= n; num++) {
    let divisorCount = 1;

    for (let i = 2; i <= num; i++) {
      if (num % i === 0) {
        divisorCount += 1;
      }
    }

    if (divisorCount >= 3) {
      count += 1;
    }
  }

  return count;
}

export {};
