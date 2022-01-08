function solution(s) {
  // 처음으로 맞는 문제 1점, 틀린 문제는 0점
  // n번 연속으로 맞으면 n점
  let arr = s.split("").map(v => +v);
  let acc = 0;
  let result = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 1) {
      result += (acc + arr[i])
      acc++;
    } else {
      acc = 0;
    }
  }
  return result
}

console.log(solution("1011100110"))