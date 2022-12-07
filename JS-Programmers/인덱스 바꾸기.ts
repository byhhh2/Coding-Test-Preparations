function solution(my_string: string, num1: number, num2: number) {
  let arr = my_string.split('');
  let tmp = arr[num1];
  arr[num1] = arr[num2];
  arr[num2] = tmp;

  return arr.join('');
}

console.log(solution('I love you', 3, 6));

export {};
