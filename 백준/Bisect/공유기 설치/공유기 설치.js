const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./공유기 설치.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const [N, C] = input[0].split(" ").map((x) => +x);

const arr = input
  .slice(1)
  .map((x) => +x)
  .sort((a, b) => a - b);

let answer = 0;

let left = 1;
let right = arr[N - 1] - arr[0];
let mid;

while (left <= right) {
  mid = Math.floor((left + right) / 2);
  let last = arr[0];
  let count = 1;

  for (let i = 1; i < N; i++) {
    if (arr[i] - last >= mid) {
      last = arr[i];
      count++;
    }
  }

  //설치 가능한 경우
  if (count >= C) {
    left = mid + 1;
    answer = mid;
  } else {
    right = mid - 1;
  }
}

console.log(answer);

function bisect(target) {
  let left = 0;
  let right = N - 1;
  let min = Infinity;
  let answer = -1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let cur = arr[mid];

    if (Math.abs(target - cur) < min) {
      min = Math.abs(target - cur);
      answer = mid;
    }

    if (cur == target) return mid;
    if (cur > target) right = mid - 1;
    if (cur < target) left = mid + 1;
  }

  return answer;
}

// left를 반환하는 경우: 가장 가까운 큰 수 반환. -> 최댓값 보다 크면 length, 작으면 0
// mid를 반환하는 경우: 가장 가까운 큰 수 반환. -> 최댓값 보다 크면 마지막 값, 작으면 0
// right를 반환하는 경우: 가장 가까운 작은 수 반환. -> 최댓값 보다 크면 마지막 값, 작으면 -1
