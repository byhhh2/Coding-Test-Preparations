function solution(array: number[]) {
  let max = Math.max(...array);

  return [max, array.indexOf(max)];
}

export {};
