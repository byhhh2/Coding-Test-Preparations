function solution(order: number) {
  return (String(order).match(/[369]/g) || []).length;
}

console.log(solution(29423));

export {};
