const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./랜선자르기.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

//가지고 있는 갯수, 필요한 갯수
const [K, N] = input[0].split(" ");

const pipes = input.slice(1).map((x) => +x);
let left = 1;
let right = Math.max(...pipes);
let mid;
let sum;

while (left <= right) {
  mid = Math.floor((left + right) / 2);
  sum = pipes.reduce((res, pipe) => res + Math.floor(pipe / mid), 0);
  if (sum < N) right = mid - 1;
  if (sum >= N) left = mid + 1;
}

console.log(right);
