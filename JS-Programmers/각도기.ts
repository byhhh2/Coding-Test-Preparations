function solution(angle: number) {
  switch (true) {
    case angle < 90:
      return 1;

    case angle === 90:
      return 2;

    case angle > 90 && angle < 180:
      return 3;

    case angle === 180:
      return 4;
  }
}

console.log(solution(70));

export {};
