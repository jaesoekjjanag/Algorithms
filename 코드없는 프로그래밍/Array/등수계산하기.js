function solution(arr) {
  let hash = {}
  let result = []

  let og = [...arr]
  arr.sort((a, b) => b - a)

  for (let i of arr) {
    hash[i] = arr.indexOf(i) + 1;
  }
  for (let i of og) {
    result.push(hash[i])
  }
  return result
}

console.log(solution([87, 89, 92, 100, 100, 76]))