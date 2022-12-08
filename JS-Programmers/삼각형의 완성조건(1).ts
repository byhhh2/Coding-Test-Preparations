function solution(sides: number[]) {
  let arr = sides.sort((a, b) => a - b);
  let [a, b, c] = arr;

  return a + b > c ? 1 : 2;
}

solution([111, 12, 1]);

export {};
