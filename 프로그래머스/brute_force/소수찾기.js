function solution(numbers) {
  function isPrimeNumber(n) {
    if (n < 2) return false;

    for (let i = 2; i <= Math.sqrt(n); ++i) {
      if (n % i === 0) return false;
    }

    return true;
  }

  const s = new Set();

  function permutation(num, indices, length) {
    if (indices.length === length) {
      const v = +indices.reduce((acc, x) => {
        return acc + num[x];
      }, "");

      s.add(v);
    }

    for (let index in num) {
      if (!indices.includes(index)) {
        permutation(num, [...indices, index], length);
      }
    }
  }

  for (let i = 1; i <= numbers.length; ++i) {
    permutation(numbers, [], i);
  }

  return [...s].reduce((acc, x) => acc + isPrimeNumber(x), 0);
}
