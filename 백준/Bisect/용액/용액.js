const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./용액.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const N = +input[0]; // 10만
const liqs = input[1].split(" ").map((x) => +x);

let left = 0;
let right = N - 1;
let feat = 2000000000;
let answer;

while (left < right) {
  const sum = liqs[left] + liqs[right];
  const abs = Math.abs(sum);
  if (abs < feat) {
    answer = [liqs[left], liqs[right]];
    feat = abs;
  }

  if (sum < 0) ++left;
  else if (sum > 0) --right;
  else break;
}

console.log(answer.join(" "));
