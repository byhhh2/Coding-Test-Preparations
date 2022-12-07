function solution(s: string) {
  let history: { [key: string]: number } = {};
  let answer: string[] = [];

  for (let elem of s) {
    if (elem in history) {
      history[elem] += 1;
    } else {
      history[elem] = 1;
    }
  }

  for (let elem in history) {
    if (history[elem] === 1) {
      answer.push(elem);
    }
  }

  return answer.sort().join('');
}

console.log(solution('abdc'));

export {};
