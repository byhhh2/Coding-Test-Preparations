function solution(babbling: string[]) {
  let babblingCount = 0;
  let babblingCategory = ['aya', 'ye', 'woo', 'ma'];

  babbling.forEach(input => {
    let saveInput = input;

    babblingCategory.forEach(word => {
      saveInput = saveInput.replaceAll(word, '*');
    });

    saveInput = saveInput.replaceAll('*', '');

    if (saveInput.length === 0) {
      babblingCount += 1;
    }
  });

  return babblingCount;
}

let b1 = ['aya', 'yee', 'u', 'maa', 'wyeoo'];
let b2 = ['ayaye', 'uuuma', 'ye', 'yemawoo', 'ayaa'];

console.log(solution(b1));
