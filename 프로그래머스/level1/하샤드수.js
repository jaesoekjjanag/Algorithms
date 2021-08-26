function solution(x) {
  const arr = String(x).split('')
  const sum = arr.map(v => +v).reduce((a, b) => a + b)
  return x % sum == 0 ? true : false
}

console.log(solution(12))