function getGCD(a: number, b: number) {
  let tmp: number;
  let n: number;
  let tmpA = a;
  let tmpB = b;

  if (tmpA < tmpB) {
    tmp = tmpA;
    tmpA = tmpB;
    tmpB = tmp;
  }

  while (tmpB != 0) {
    n = tmpA % tmpB;
    tmpA = tmpB;
    tmpB = n;
  }

  return tmpA;
}

function solution(dots: number[][]) {
  for (let index = 1; index < dots.length; index++) {
    let one = [dots[0], dots[index]];
    let other = dots.filter((dot, i) => i !== 0 && i !== index);

    let oneDx = one[0][0] - one[1][0];
    let oneDy = one[0][1] - one[1][1];
    let otherDx = other[0][0] - other[1][0];
    let otherDy = other[0][1] - other[1][1];
    let gcd = getGCD(oneDx, oneDy);

    oneDx /= gcd;
    oneDy /= gcd;

    gcd = getGCD(otherDx, otherDy);

    otherDx /= gcd;
    otherDy /= gcd;

    if (oneDx * oneDy === otherDx * otherDy) {
      return 1;
    }
  }

  return 0;
}

let t1 = [
  [1, 4],
  [9, 2],
  [3, 8],
  [11, 6],
];
let t2 = [
  [3, 5],
  [4, 1],
  [2, 4],
  [5, 10],
];

console.log(solution(t1));

export {};
