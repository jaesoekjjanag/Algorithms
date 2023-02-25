const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "./가장 긴 증가하는 부분 수열.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const n = +input[0];
const nums = input[1].split(" ").map((x) => +x);

// O(n^2)
// dp = Array(n).fill(0);
// dp[0] = 1;
// max = dp[0];

// for (let i = 1; i < n; i++) {
//   const last = Array.from({ length: i }, (_, j) => j)
//     .filter((j) => nums[j] < nums[i])
//     .sort((a, b) => dp[b] - dp[a]);

//   dp[i] = last.length ? dp[last[0]] + 1 : 1;
//   max = Math.max(max, dp[i]);
// }

// console.log(max);

// O(nlogn) 이분탐색
const lowerBound = (target, arr) => {
  let left = 0;
  let right = arr.length;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    const value = arr[mid];
    if (target <= value) right = mid;
    if (target > value) left = mid + 1;
  }

  return right;
};

const dp = [nums[0]];

for (let i = 1; i < n; i++) {
  const num = nums[i];
  const index = lowerBound(num, dp);

  if (!dp[index] || num < dp[index]) dp[index] = num;
}

console.log(dp.length);
