function solution(A, B) {
  let clone = A;
  let count = 0;

  for (let i = 0; i < A.length; i++) {
    if (clone === B) {
      return count;
    }

    let last = clone.slice(-1);
    clone = last + clone.slice(0, A.length - 1);
    count += 1;
  }

  return -1;
}

console.log(solution('hello', 'ohell'));
