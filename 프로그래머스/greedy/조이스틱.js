function solution(name) {
  const diff = [...name].map((x) => {
    const code = x.charCodeAt();
    return Math.min(code - 65, 90 - code + 1);
  });

  const sum = diff.reduce((a, b) => a + b);

  let move = name.length - 1;
  for (let i = 0; i < name.length; i++) {
    if (diff[i]) continue;
    let seq = i; //2
    while (diff[seq] === 0) ++seq; //4

    const left = i > 1 ? i - 1 : 0;
    const right = name.length - seq;

    move = Math.min(move, 2 * left + right, 2 * right + left);
    i = seq - 1;
  }

  return move + sum;
}

console.log(solution("JEROEN"));
console.log(solution("A"));
console.log(solution("JAN"));
