function solution(my_string: string) {
  let sum = 0;

  for (let str of my_string) {
    if (!Number.isNaN(+str)) {
      sum += +str;
    }
  }

  return sum;
}

let t1 = 'aAb1B2cC34oOp';

console.log(solution(t1));

export {};
