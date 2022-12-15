function solution(keyinput: string[], board: number[]) {
  let x = 0;
  let y = 0;
  let [width, height] = board;

  let limit = {
    left: -Math.floor(width / 2),
    right: Math.floor(width / 2),
    up: Math.floor(height / 2),
    down: -Math.floor(height / 2),
  };

  for (let key of keyinput) {
    switch (key) {
      case 'left':
        if (x > limit.left) x -= 1;
        continue;

      case 'right':
        if (x < limit.right) x += 1;
        continue;

      case 'up':
        if (y < limit.up) y += 1;
        continue;

      case 'down':
        if (y > limit.down) y -= 1;
        continue;
    }
  }

  return [x, y];
}

let tk1 = ['left', 'right', 'up', 'right', 'right'];
let tb1 = [11, 11];
let tk2 = ['down', 'down', 'down', 'down', 'down'];
let tb2 = [7, 9];

console.log(solution(tk2, tb2));

export {};
