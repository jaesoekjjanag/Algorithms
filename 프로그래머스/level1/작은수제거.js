function solution(arr) {
  const min = Math.min.apply(null, arr)
  while (arr.includes(min)) {
    arr.splice(arr.indexOf(min), 1)
  }
  return arr
}

console.log(solution([4, 3, 2, 1, 1]))