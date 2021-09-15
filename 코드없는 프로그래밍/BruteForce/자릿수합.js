function solution(arr) {
  //max[0]에는 원본 숫자, max[1]에는 합친 숫자
  let max = [0, 0]
  for (let i = 0; i < arr.length; i++) {
    let sum = String(arr[i]).split('').map(v => +v).reduce((a, b) => a + b)
    if (max[1] <= sum) {
      if (max[1] === sum && max[0] < sum) {
        //원래 값이 더 크면 아무것도 하지 않음
        continue
      }
      max[0] = arr[i]
      max[1] = sum
    }
  }
  console.log(max)
}

solution([131, 111, 99, 882])