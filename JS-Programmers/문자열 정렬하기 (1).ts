function solution(my_string: string) {
  let nums: number[] = [];

  for (let str of my_string) {
    if (!Number.isNaN(+str)) {
      nums.push(+str);
    }
  }

  return nums.sort((a, b) => a - b);
}

console.log(solution('hi12392'));

export {};
