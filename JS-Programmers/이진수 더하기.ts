function solution(bin1: string, bin2: string) {
  let a = 0;
  let b = 0;
  let c = 0;
  let answer = '';

  for (let i = bin1.length - 1; i >= 0; i--) {
    a += Number(bin1[i]) * 2 ** (bin1.length - 1 - i);
  }

  for (let i = bin2.length - 1; i >= 0; i--) {
    b += Number(bin2[i]) * 2 ** (bin2.length - 1 - i);
  }

  c = a + b;

  while (c > 1) {
    answer = String(c % 2) + answer;
    c = Math.floor(c / 2);
  }

  answer = String(c % 2) + answer;

  return answer;
}

let t1bin1 = '10';
let t1bin2 = '11';
let t2bin1 = '1001';
let t2bin2 = '1111';

console.log(solution(t2bin1, t2bin2));

export {};
