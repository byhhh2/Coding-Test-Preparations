function solution(my_string: string, n: number) {
  let answer = '';

  for (let str of my_string) {
    answer += str.repeat(n);
  }

  return answer;
}

console.log(solution('hello', 3));

export {};
