function solution(my_string: string) {
  let str = my_string;

  [...str].forEach(char => {
    str = str.replaceAll(char, '*');
    str = str.replace('*', char);
    str = str.replaceAll('*', '');
  });

  return str;
}

let t1 = 'people';
let t2 = 'We are the world';

console.log(solution(t1));

export {};
