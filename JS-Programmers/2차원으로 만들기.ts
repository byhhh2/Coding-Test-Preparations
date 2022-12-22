function solution(num_list: number[], n: number) {
  let answer: number[][] = [];
  let start = 0,
    end = n;

  while (end <= num_list.length) {
    answer.push(num_list.slice(start, end));

    start += n;
    end += n;
  }

  return answer;
}

let tl1 = [1, 2, 3, 4, 5, 6, 7, 8];
let tn1 = 2;

let tl2 = [100, 95, 2, 4, 5, 6, 18, 33, 948];
let tn2 = 3;

console.log(solution(tl2, tn2));

export {};
