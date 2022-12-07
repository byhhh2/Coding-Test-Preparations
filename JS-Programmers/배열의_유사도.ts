function solution(s1: string[], s2: string[]) {
  let count = 0;

  for (let elem of s1) {
    if (s2.includes(elem)) {
      count += 1;
    }
  }

  return count;
}

export {};
