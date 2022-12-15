function solution(n: number) {
  let num = 0;
  let fac = 1;

  while (fac <= n) {
    num += 1;
    fac = fac * num;
  }

  return num - 1;
}

let t1 = 3628800;
let t2 = 7;

console.log(solution(t2));

export {};
