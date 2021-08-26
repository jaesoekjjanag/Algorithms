function solution(n, m) {
  let max = 1
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= m; j++) {
      if (n % i == 0 && m % j == 0 && i == j) {
        if (max < i) {
          max = i
        }
      }
    }
  }
  let min = n * m / max
  return [max, min]
}

console.log(solution(8, 36))