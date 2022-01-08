function solution(n, arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    let top = arr[i - n] ? arr[i - n] : 0;
    let left = arr[i - 1] ? arr[i - 1] : 0
    let right = arr[i + 1] ? arr[i + 1] : 0
    let bottom = arr[i + n] ? arr[i + n] : 0

    // 배열의 양 끝인 경우
    if (i % (n) === n - 1) right = 0;
    if (i % (n) === 0) left = 0;

    if (arr[i] > Math.max(top, left, right, bottom)) count++
  }
  return count
}

console.log(solution(5, [5, 3, 7, 2, 3, 3, 7, 1, 6, 1, 7, 2, 5, 3, 4, 4, 3, 6, 4, 1, 8, 7, 3, 5, 2]))
console.log(solution(4, [9, 3, 7, 4, 2, 4, 3, 3, 1, 8, 2, 7]))
console.log(solution(3, [1, 1, 1, 1, 1, 1, 1, 1, 1]))