function solution(s: string) {
  let arr = s.split(' ');
  let prevStr = '';
  let answer = 0;

  for (let elem of arr) {
    if (elem === 'Z') {
      answer -= +prevStr;
      continue;
    }

    answer += +elem;
    prevStr = elem;
  }

  return answer;
}

let t1 = '1 2 Z 3';
let t2 = '10 20 30 40';
let t3 = '10 Z 20 Z 1';

console.log(solution(t3));

export {};
