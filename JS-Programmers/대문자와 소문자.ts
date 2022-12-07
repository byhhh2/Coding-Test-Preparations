function solution(my_string: string) {
  let answer: string[] = [];

  for (let i = 0; i < my_string.length; i++) {
    if (my_string.charCodeAt(i) - 97 >= 0) {
      answer.push(my_string[i].toUpperCase());
    } else {
      answer.push(my_string[i].toLowerCase());
    }
  }

  return answer.join('');
}

console.log(solution('cccCCC'));

export {};
