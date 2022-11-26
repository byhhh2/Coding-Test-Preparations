function solution(common) {
  let [first, second, third] = common;

  if (first + third === second * 2) {
    return common.at(-1) + (third - second);
  } else {
    return common.at(-1) * (third / second);
  }
}

let t1 = [1, 2, 3, 4];
let t2 = [2, 4, 8];

console.log(solution(t1));

export {};
