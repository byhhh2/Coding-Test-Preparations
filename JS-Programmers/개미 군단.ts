function solution(hp: number) {
  let count = 0;
  let ants = [5, 3, 1];

  for (const ant of ants) {
    count += Math.floor(hp / ant);
    hp = hp % ant;

    if (hp <= 0) {
      break;
    }
  }

  return count;
}

let t1 = 23;
let t2 = 24;
let t3 = 999;

console.log(solution(t2));

export {};
