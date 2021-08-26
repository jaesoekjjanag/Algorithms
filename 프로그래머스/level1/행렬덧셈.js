function solution(arr1, arr2) {
  var answer = [];
  const r = arr1.length
  const c = arr1[0].length

  for (let i = 0; i < r; i++) {
    const row = []
    for (let j = 0; j < c; j++) {
      row.push(arr1[i][j] + arr2[i][j])
    }
    answer.push(row)
  }
  return answer;
}