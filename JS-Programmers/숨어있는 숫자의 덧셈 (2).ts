function solution(my_string: string) {
  let sum = 0;
  let num = '';

  for (let str of my_string) {
    if (!Number.isNaN(+str)) {
      num += str;
    } else {
      sum += +num;
      num = '';
    }
  }

  return sum + +num;
}

let t1 = 'aAb1B2cC34oOp';
let t2 = '1a2b3c4d123Z';
let t3 = 'dsadsad';
let t4 = 'asdawqe34';

console.log(solution(t4));

export {};
