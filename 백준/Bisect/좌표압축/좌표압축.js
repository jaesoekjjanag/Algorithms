const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./좌표압축.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const N = +input[0];
const nums = input[1].split(" ").map((x) => +x);

const set = [...new Set(nums)].sort((a, b) => a - b);

function bisect(t, arr) {
  let left = 0;
  let right = arr.length - 1;
  let mid;

  while (left <= right) {
    mid = Math.floor((left + right) / 2);
    cur = arr[mid];
    if (cur === t) return mid;
    if (cur > t) right = mid;
    if (cur < t) left = mid + 1;
  }
}

console.log(nums.map((x) => bisect(x, set)).join(" "));
