const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./가장 큰 증가 부분 수열.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const n = +input[0];
const nums = input[1].split(" ").map((x) => +x);

dp = Array(n).fill(0);
dp[0] = nums[0];
max = dp[0];

for (let i = 1; i < n; i++) {
  const num = nums[i];

  // 이전까지의 num 중에서 현재 num보다 작고, dp가 최대인 값
  const last = Array.from({ length: i }, (_, index) => index).sort(
    (a, b) => dp[b] - dp[a]
  );

  for (let j = 0; j < i; j++) {
    const index = last[j];

    if (nums[index] < num) {
      dp[i] = dp[index] + num;
      break;
    }

    if (j == i - 1) {
      dp[i] = num;
    }
  }
  max = Math.max(max, dp[i]);
}

console.log(max);
