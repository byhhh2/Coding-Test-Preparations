function solution(quiz: string[]) {
  let answer: string[] = [];

  for (let question of quiz) {
    let [a, b, c] = question
      .replace(' + ', ',')
      .replace(' - ', ',')
      .replace(' = ', ',')
      .split(',')
      .map(elem => Number(elem));

    if (question.includes('+') ? a + b === c : a - b === c) {
      answer.push('O');
      continue;
    }

    answer.push('X');
  }

  return answer;
}

let t1 = ['3 - 4 = -3', '5 + 6 = 11'];
let t2 = ['19 - 6 = 13', '5 + 66 = 71', '5 - 15 = 63', '3 - 1 = 2'];

console.log(solution(t2));

export {};
