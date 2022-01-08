function solution(arr) {
  bigger = [];
  bigger.push(arr[0])
  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && arr[i] > arr[i - 1]) {
      bigger.push(arr[i])
    }
  }
  return bigger.join(' ')
}

console.log(solution([7, 3, 9, 5, 6, 12]))