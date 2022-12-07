function solution(array: number[]) {
  let count = 0;

  for (let elem of array) {
    let current = String(elem);

    count += (current.match(/7/g) || []).length;
  }

  return count;
}

let t1 = [7, 77, 17];
let t2 = [10, 29];

console.log(solution(t2));

export {};
