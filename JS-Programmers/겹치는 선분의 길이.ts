function solution(lines: number[][]) {
  let allLines: { [key in string]: number } = {};
  let count = 0;

  for (let line of lines) {
    let [start, end] = line;

    for (let point = start; point < end; point++) {
      let key = `${[point, point + 1]}`;

      if (key in allLines) {
        allLines[key] += 1;
      } else {
        allLines[key] = 1;
      }
    }
  }

  for (let line in allLines) {
    if (allLines[line] >= 2) {
      count += 1;
    }
  }

  return count;
}

let t1 = [
  [0, 2],
  [-3, -1],
  [-2, 1],
];

let t2 = [
  [0, 5],
  [3, 9],
  [1, 10],
];

console.log(solution(t2));

export {};
