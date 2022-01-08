function solution(arr) {
  let max = Number.MIN_SAFE_INTEGER;
  let cnt = 0;
  for (let i of arr) {
    if (i > max) {
      max = i;
      cnt++;
    }
  }
  console.log(cnt);
}

solution([130, 135, 148, 140, 145, 150, 150, 153])