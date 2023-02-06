const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./숫자카드.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

let [N, has, M, nums] = input;

const set = new Set(has.split(" "));
console.log(
  nums
    .split(" ")
    .map((x) => +set.has(x))
    .join(" ")
);

has = has
  .split(" ")
  .sort((a, b) => a - b)
  .map((x) => +x);

function bisect(num) {
  let left = 0;
  let right = has.length - 1;
  let mid, cur;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    cur = has[mid];

    if (cur === num) return 1;
    if (cur < num) left = mid + 1;
    if (cur > num) right = mid - 1;
  }

  return 0;
}

console.log(
  nums
    .split(" ")
    .map((x) => bisect(+x))
    .join(" ")
);
