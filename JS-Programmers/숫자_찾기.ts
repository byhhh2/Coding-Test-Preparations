function solution(num: number, k: number) {
  let index = String(num).indexOf(String(k));

  return index === -1 ? index : index + 1;
}

console.log(solution(123456, 7));

export {};
