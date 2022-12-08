function solution(i: number, j: number, k: number) {
  let strK = String(k);
  let count = 0;

  for (let num = i; num <= j; num++) {
    count += (String(num).match(new RegExp(strK, 'g')) || []).length;
  }

  return count;
}

console.log(solution(1, 13, 1));

export {};
