function solution(numbers: number[], k: number) {
  let index = -2;

  for (let turn = 1; turn <= k; turn++) {
    index += 2;
  }

  return numbers[index % numbers.length];
}

export {};
