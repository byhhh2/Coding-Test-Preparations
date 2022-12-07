function solution(cipher: string, code: number) {
  var answer = '';

  for (let i = code - 1; i < cipher.length; i += code) {
    answer += cipher[i];
  }

  return answer;
}

console.log(solution('dfjardstddetckdaccccdegk', 4));

export {};
