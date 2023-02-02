function solution(N, number) {
  if (N === number || N === 1) return (N % number) + 1;

  const visited = Array(320001).fill(0);
  const dp = Array.from({ length: 9 }, () => []);

  for (let i = 1; i < 6; i++) {
    const num = +("" + N).repeat(i);
    if (num <= 32000) {
      dp[i].push(num);
      visited[num] = i;
    }
  }

  const operators = ["+", "-", "/", "*"];
  const getNext = (a, b) => {
    const result = new Set();
    let res;
    for (let o of operators) {
      res1 = eval(a + o + b);
      res2 = eval(b + o + a);
      if (res1 >= 1 && res1 <= 32000) result.add(parseInt(res1));

      if (res2 >= 1 && res2 <= 32000) result.add(parseInt(res2));
    }
    return [...result];
  };

  for (let i = 2; i <= 8; i++) {
    for (let j = 1; j <= i / 2; j++) {
      for (let a of dp[j]) {
        for (let b of dp[i - j]) {
          for (let n of getNext(a, b)) {
            if (n === number) {
              if (i > 8) return -1;
              return i;
            }
            if (!visited[n]) {
              dp[i].push(n);
              visited[n] = i;
            }
          }
        }
      }
    }
  }

  return -1;
}
