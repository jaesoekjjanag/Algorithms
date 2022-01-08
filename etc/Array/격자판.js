function solution(arr) {
  let max = 0;
  let c1 = 0, c2 = 0;
  for (let i = 0; i < arr.length; i++) {
    let column = 0;
    let row = 0;
    for (let j = 0; j < arr.length; j++) {
      column += arr[j][i];
      row += arr[i][j];
      if (i == j) {
        c1 += arr[i][j];
      }
      if (i + j == arr.length - 1) c2 += arr[i][j];
    }
    if (max < row) max = row;
    if (max < column) max = column;
  }
  return Math.max(max, c1, c2)
}

console.log(solution([[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15], [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]))
console.log(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))