function solution(sides: number[]) {
  let [one, other] = sides;
  let remainder = 0;
  let candidate: number[] = [];

  if (one < other) {
    let tmp = one;
    one = other;
    other = tmp;
  }

  // 1. one이 가장 긴 변인 경우
  remainder = one - other + 1;

  while (remainder <= one) {
    candidate.push(remainder++);
  }

  // 2. 나머지가 가장 긴 변인 경우
  remainder = one + 1;

  while (remainder < one + other) {
    candidate.push(remainder++);
  }

  return candidate.length;
}

console.log(solution([1, 2]));

export {};
