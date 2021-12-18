function solution(arr) {
  for (let i = 1; i < arr.length; i++) {
    let temp = arr[i], j;
    for (j = i - 1; j >= 0; j--) {
      if (arr[j] > temp) arr[j + 1] = arr[j];
      else break;
    }
    arr[j + 1] = temp
  }
  return arr
}
console.log(solution([3, 7, 5, 6, 10, 9]))