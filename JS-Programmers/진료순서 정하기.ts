function solution(emergency: number[]) {
  let rank = 1;
  let originEmergency = [...emergency];
  let rankEmergency = [...emergency];
  let sortedEmergency = emergency.sort((a, b) => b - a);

  for (let elem of sortedEmergency) {
    rankEmergency[originEmergency.indexOf(elem)] = rank++;
  }

  return rankEmergency;
}

let t1 = [3, 76, 24];
let t2 = [1, 2, 3, 4, 5, 6, 7];

console.log(solution(t2));

export {};
