function solution(numlist: number[], n: number) {
  let targetList = [...numlist];

  targetList.sort((a, b) => {
    if (Math.abs(a - n) === Math.abs(b - n)) {
      return b - a;
    }

    return Math.abs(a - n) - Math.abs(b - n);
  });

  return targetList;
}

let t1 = [1, 2, 3, 4, 5, 6];
let t2 = [10000, 20, 36, 47, 40, 6, 10, 7000];

console.log(solution(t1, 4));

export {};
