function solution(numbers: number[]) {
  let max = numbers[0] * numbers[1];

  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      if (numbers[i] * numbers[j] > max) {
        max = numbers[i] * numbers[j];
      }
    }
  }

  return max;
}

console.log(solution([10, 20, 30, 5, 5, 20, 5]));

export {};
