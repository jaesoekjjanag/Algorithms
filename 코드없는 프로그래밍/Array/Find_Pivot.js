function solution(arr) {
  let right = arr.reduce((a, b) => a + b)
  let left = 0
  let past = 0
  for (let i = 0; i < arr.length; i++) {
    right -= arr[i]  //30
    left += past //0
    if (left == right) return i;
    past = arr[i]  //
  }
  return -1
}

console.log(solution([1, 8, 2, 9, 2, 3, 6]))