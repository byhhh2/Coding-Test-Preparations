function solution(score: number[][]) {
  let scores = [...score];
  let prevScore = -1;
  let rank = 0;
  let continuousCount = 0;

  for (let studentIndex in scores) {
    let [eng, math] = scores[studentIndex];
    scores[studentIndex] = [eng + math, Number(studentIndex)];
  }

  scores.sort((a, b) => b[0] - a[0]);

  for (let score of scores) {
    let [currentScore] = score;

    if (currentScore !== prevScore) {
      prevScore = currentScore;
      rank += 1 + continuousCount;
      continuousCount = 0;
      score.push(rank);
      continue;
    }

    continuousCount += 1;
    score.push(rank);
  }

  scores.sort((a, b) => a[1] - b[1]);

  return scores.map(score => score[2]);
}

let t1 = [
  [80, 70],
  [90, 50],
  [40, 70],
  [50, 80],
];
let t2 = [
  [80, 70],
  [70, 80],
  [30, 50],
  [90, 100],
  [100, 90],
  [100, 100],
  [10, 30],
];

console.log(solution(t2));

export {};
