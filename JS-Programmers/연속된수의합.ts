function solution(num, total) {
  let base = Math.floor(total / num);
  let baseArray = Array(num).fill(base);
  let diff = Math.floor(num / 2) * -1;

  for (let i in baseArray) {
    baseArray[i] += baseArray.length % 2 === 0 ? ++diff : diff++;
  }

  return baseArray;
}

/**
 * 
 * num	total	result
    3	12	[3, 4, 5]
    5	15	[1, 2, 3, 4, 5] 
    4	14	[2, 3, 4, 5]
    5	5	[-1, 0, 1, 2, 3]
 */

console.log(solution(3, 12));

export {};
