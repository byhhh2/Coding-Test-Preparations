function solution(dot: number[]) {
  let [x, y] = dot;

  switch (true) {
    case x > 0 && y > 0:
      return 1;

    case x < 0 && y > 0:
      return 2;

    case x < 0 && y < 0:
      return 3;

    case x > 0 && y < 0:
      return 4;
  }
}

let t1 = [2, 4];

console.log(solution(t1));

export {};
