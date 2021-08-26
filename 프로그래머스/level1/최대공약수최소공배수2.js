function solution(a, b) {
  const small = Math.min(a, b)
  const big = Math.max(a, b)

  if (a == 0 || b == 0) {
    return big
  }
  return solution(small, big % small)
}
