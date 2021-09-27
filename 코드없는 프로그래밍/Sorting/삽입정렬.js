function solution(arr) {
  for (let i = 1; i < arr.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      arr[j + 1] = arr[j]
      if (arr[j] < arr[i]) {
        arr[j] = arr[i]
      }
    }
  }
  console.log(arr)
}

solution([11, 7, 5, 6, 10, 9])