const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./합이0.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const N = +input[0]; // 10만
const participants = input[1]
  .split(" ")
  .map((x) => +x)
  .sort((a, b) => a - b);

function search(target, left) {
  let right = N - 1;
  let sum;
  let count = 0;

  while (left < right) {
    sum = participants[left] + participants[right];
    if (sum > target) right--;
    else if (sum < target) left++;
    else {
      const lValue = participants[left];
      const rValue = participants[right];
      if (lValue === rValue) {
        count += ((right - left) * (right - left + 1)) / 2;
        break;
      }

      let lCount = 1;
      let rCount = 1;

      while (left < right && participants[++left] == lValue) {
        lCount++;
      }
      while (left < right && participants[right - 1] == rValue) {
        right--;
        rCount++;
      }

      count += lCount * rCount;
    }
  }

  return count;
}

console.log(
  participants.reduce((acc, p, i) => {
    if (p > 0) return acc;
    return acc + search(-p, i + 1);
  }, 0)
);
