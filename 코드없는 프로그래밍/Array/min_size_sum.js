function solution(arr, t) {
  let length = Infinity
  let start = 0
  let acc = 0
  //! i는 end 포인터
  for (let i = 0; i < arr.length; i++) {
    acc += arr[i];
    if (acc == t && (i - start + 1) < length) length = i - start + 1;
    if (acc > t) {
      acc -= arr[i];
      start += 1;
    }
  }
  return length
}

console.log(solution([7, 4, 2, 1, 3, 2], 7))