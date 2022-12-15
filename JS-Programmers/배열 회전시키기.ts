function solution(numbers: number[], direction: string) {
  switch (direction) {
    case 'left':
      let left = numbers.shift()!;
      numbers.push(left);
      return numbers;

    case 'right':
      let right = numbers.pop()!;
      numbers = [right, ...numbers];
      return numbers;
  }
}

export {};
