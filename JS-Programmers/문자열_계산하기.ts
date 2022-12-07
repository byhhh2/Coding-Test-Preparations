function solution(my_string: string) {
  let statement = my_string.split(' ');
  let answer = Number(statement.shift());

  for (let index = 0; index < statement.length; index += 2) {
    if (statement[index] === '+') {
      answer += Number(statement[index + 1]);
    } else if (statement[index] === '-') {
      answer -= Number(statement[index + 1]);
    }

    if (index > statement.length) {
      return answer;
    }
  }

  return answer;
}

let t1 = '3 + 2 - 1 + 5 - 12 + 3';

console.log(solution(t1));

export {};
