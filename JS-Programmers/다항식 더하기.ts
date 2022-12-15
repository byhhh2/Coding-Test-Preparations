function solution(polynomial: string) {
  let terms = polynomial.replaceAll(' ', '').split('+');

  let sumDegree1 = 0;
  let sumDegree0 = 0;

  let degree1 = terms.filter(elem => elem.includes('x'));
  let degree0 = terms.filter(elem => !elem.includes('x'));

  for (let term of degree1) {
    let num = term.replace('x', '');

    sumDegree1 += num === '' ? 1 : +num;
  }

  for (let term of degree0) {
    sumDegree0 += +term;
  }

  switch (true) {
    case sumDegree1 !== 0 && sumDegree0 !== 0:
      return `${sumDegree1 === 1 ? '' : sumDegree1}x + ${sumDegree0}`;

    case sumDegree1 !== 0 && sumDegree0 === 0:
      return `${sumDegree1 === 1 ? '' : sumDegree1}x`;

    case sumDegree0 !== 0:
      return `${sumDegree0}`;
  }
}

let t1 = '3x + 7 + x';
let t2 = 'x + x + x';
let t3 = '1';
let t4 = '1 + 2 + 3';
let t5 = 'x';

console.log(solution(t5));

export {};
