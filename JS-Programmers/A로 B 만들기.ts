function solution(before: string, after: string) {
  let sortedBefore = [...before].sort().join('');
  let sortedAfter = [...after].sort().join('');

  return sortedBefore === sortedAfter ? 1 : 0;
}

console.log(solution('olleh', 'hello'));

export {};
