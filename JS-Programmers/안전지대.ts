function solution(board: number[][]) {
  let count = 0;

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === 1) {
        if (i - 1 >= 0 && board[i - 1][j] !== 1) {
          board[i - 1][j] = -1;
        }

        if (i + 1 < board.length && board[i + 1][j] !== 1) {
          board[i + 1][j] = -1;
        }

        if (j - 1 >= 0 && board[i][j - 1] !== 1) {
          board[i][j - 1] = -1;
        }

        if (j + 1 < board[i].length && board[i][j + 1] !== 1) {
          board[i][j + 1] = -1;
        }

        if (i - 1 >= 0 && j - 1 >= 0 && board[i - 1][j - 1] !== 1) {
          board[i - 1][j - 1] = -1;
        }

        if (
          i + 1 < board.length &&
          j + 1 < board[i].length &&
          board[i + 1][j + 1] !== 1
        ) {
          board[i + 1][j + 1] = -1;
        }

        if (
          i - 1 >= 0 &&
          j + 1 < board[i].length &&
          board[i - 1][j + 1] !== 1
        ) {
          board[i - 1][j + 1] = -1;
        }

        if (i + 1 < board.length && j - 1 >= 0 && board[i + 1][j - 1] !== 1) {
          board[i + 1][j - 1] = -1;
        }
      }
    }
  }

  for (let row of board) {
    for (let col of row) {
      if (col === 0) {
        count += 1;
      }
    }
  }

  return count;
}

let t1 = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
];

let t2 = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0],
];

let t3 = [
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
];

console.log(solution(t1));
