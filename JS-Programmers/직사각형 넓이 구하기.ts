function solution(dots: number[][]) {
  dots.sort((a, b) => a[0] - b[0]);
  dots.sort((a, b) => a[1] - b[1]);

  let [min, , , max] = dots;

  return (max[1] - min[1]) * (max[0] - min[0]);
}

let t1 = [
  [1, 1],
  [2, 1],
  [2, 2],
  [1, 2],
];

let t2 = [
  [-1, -1],
  [1, 1],
  [1, -1],
  [-1, 1],
];

console.log(solution(t1));

export {};
