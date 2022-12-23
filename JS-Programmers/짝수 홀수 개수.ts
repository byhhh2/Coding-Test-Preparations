function solution(num_list: number[]) {
  let answer = [0, 0];

  for (let num of num_list) {
    if (num % 2 === 0) {
      answer[0] += 1;
      continue;
    }

    answer[1] += 1;
  }

  return answer;
}

export {};
