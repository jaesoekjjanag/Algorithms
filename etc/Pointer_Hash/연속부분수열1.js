//* 조건에 중복에 관한 내옹이 적혀있지 않기 때문에, 중복을 무시하고 풀었음.
//* O(n**2)
function solution(arr, m) {
  let cnt = 0;
  let ptr = 0;
  while (ptr < arr.length) {
    let acc = 0;
    for (let i = ptr; i < arr.length; i++) {
      acc += arr[i];
      if (i === arr.length - 1 && acc < m) {
        return cnt;
      }
      if (acc == m) {
        cnt++
        ptr++
        break;
      }
      if (acc > m) {
        ptr++;
        break;
      }
    }
  }
  return cnt
}
console.log(solution([1, 2, 1, 3, 1, 1, 1, 2], 6))

//* 2 pointer
function solution2(arr, m) {
  let cnt = 0; lt = 0, sum = 0;
  for (let rt = 0; rt < arr.length; rt++) {
    sum += arr[rt];
    if (sum === m) cnt++;
    while (sum >= m) {
      sum -= arr[lt++];
      if (sum === m) {
        sum -= arr[lt++];
        if (sum === m) answer++;
      }
    }
  }
}
