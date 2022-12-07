function solution(array: number[], n: number) {
  let [min] = array;
  let minDiff = Math.abs(n - min);

  for (let elem of array) {
    if (minDiff === Math.abs(n - elem)) {
      if (min > elem) {
        min = elem;
        minDiff = Math.abs(n - elem);
        continue;
      }
    }

    if (minDiff > Math.abs(n - elem)) {
      min = elem;
      minDiff = Math.abs(n - elem);
    }
  }

  return min;
}

let ta1 = [3, 10, 28];
let tn1 = 20;
let ta2 = [10, 11, 12];
let tn2 = 13;

console.log(solution(ta2, tn2));

export {};
