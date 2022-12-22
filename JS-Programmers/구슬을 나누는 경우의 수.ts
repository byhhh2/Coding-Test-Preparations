function solution(balls: number, share: number) {
  let count = balls - share > share ? share : balls - share;
  let parent = 1;
  let child = 1;
  let m = count;

  for (const i of Array(count).keys()) {
    parent *= balls;
    balls -= 1;

    child *= m;
    m -= 1;
  }

  return parent / child;
}

console.log(solution(6, 3));

export {};
