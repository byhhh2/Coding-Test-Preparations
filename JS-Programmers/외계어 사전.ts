function solution(spell: string[], dic: string[]) {
  let spellStr = spell.join('');

  for (let word of dic) {
    let isAllInclude = true;

    for (let s of spell) {
      if (!word.includes(s)) {
        isAllInclude = false;
        break;
      }
    }

    if (isAllInclude && spellStr.length === word.length) {
      return 1;
    }
  }

  return 2;
}

export {};
