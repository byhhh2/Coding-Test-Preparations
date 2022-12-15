function solution(my_string: string) {
  return my_string
    .replaceAll('a', '')
    .replaceAll('e', '')
    .replaceAll('i', '')
    .replaceAll('o', '')
    .replaceAll('u', '');
}

export {};
