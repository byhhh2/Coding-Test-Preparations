function solution(strlist: string[]) {
  let answer: number[] = [];

  strlist.forEach(str => {
    answer.push(str.length);
  });

  return answer;
}

export {};
