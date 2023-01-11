function solution(brown, yellow) {
  const n = (brown - 8) / 2;

  for (let i = n; i >= 0; --i) {
    const j = n - i;
    const count = (i + 1) * (j + 1);
    if (count === yellow && i >= j) {
      return [i + 3, j + 3];
    }
  }
}
