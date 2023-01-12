function solution(word) {
  const alphabets = ["A", "E", "I", "O", "U"];
  const adder = Array(5)
    .fill(0)
    .reduce(
      (acc, x, i) => {
        const prev = acc[acc.length - 1];
        acc[i] = prev * 5 + 1;
        return acc;
      },
      [0]
    );

  return [...word].reduce((acc, x, i) => {
    return acc + alphabets.indexOf(x) * adder[4 - i] + 1;
  }, 0);
}
