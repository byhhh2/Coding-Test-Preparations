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

function solution(a: number, b: number) {
  let gcd = getGCD(a, b);
  let gcdB = b / gcd;

  for (let i = 2; i <= gcdB; i++) {
    while (gcdB % i === 0) {
      if (i !== 2 && i !== 5) {
        return 2;
      }
      gcdB /= i;
    }
  }

  return 1;
}

console.log(solution(12, 21));

export {};
