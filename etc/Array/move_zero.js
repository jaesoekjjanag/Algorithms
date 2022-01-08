function solution(arr) {
  let ptr = 0    //! 0을 찾는 포인터
  for (let i = 0; i < arr.length; i++) {  //!: 0이 아닌 값을 찾는 포인터
    if (arr[i] !== 0) {
      [arr[ptr], arr[i]] = [arr[i], arr[ptr]]
      ptr += 1
    }
  }
  return arr
}

console.log(solution([0, 5, 0, 7, 6, 3]))