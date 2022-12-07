function solution(my_str: string, n: number) {
  let remainder = my_str;
  let answer: string[] = [];

  for (let i = 0; i < Math.ceil(my_str.length / n); i++) {
    answer.push(remainder.slice(0, n));
    remainder = remainder.slice(n);
  }

  return answer;
}

let ts1 = 'abc1Addfggg4556b';
let tn1 = 6;
let ts2 = 'abcdef123';
let tn2 = 3;

console.log(solution(ts2, tn2));

export {};
