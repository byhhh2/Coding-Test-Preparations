function solution(my_string: string) {
  return my_string.toLowerCase().split('').sort().join('');
}

let t1 = 'Bcad';
let t2 = 'heLLo';

console.log(solution(t2));

export {};
