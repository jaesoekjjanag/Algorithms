const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./세용액.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const N = +input[0]; // 10만
const liqs = input[1]
  .split(" ")
  .map((x) => +x)
  .sort((a, b) => a - b);

let feat = 3000000000;

function twoPointer(target, i) {
  let left = i + 1;
  let right = N - 1;

  while (left < right) {
    let total = target + liqs[left] + liqs[right];

    if (feat > Math.abs(total)) {
      feat = Math.abs(total);
      answer = [target, liqs[left], liqs[right]];
    }

    if (total > 0) {
      right -= 1;
    } else {
      left += 1;
    }
  }
}

liqs.forEach((x, i) => twoPointer(x, i));
console.log(answer.join(" "));


// for (let i = 0; i < N - 2; ++i) {
//   for (let j = i + 1; j < N - 1; ++j) {
//     target = liqs[i] + liqs[j];

//     temp = bisect(target, j + 1);
//     if (temp) {
//       answer = [liqs[i], liqs[j], liqs[temp]];
//     }
//   }
// }

// console.log(answer.join(" "));

// function bisect(target, left) {
//   let right = N - 1;
//   let index;

//   while (left <= right) {
//     mid = Math.floor((left + right) / 2);
//     sum = liqs[mid] + target;

//     if (Math.abs(sum) < feat) {
//       feat = Math.abs(sum);
//       index = mid;
//     }

//     if (sum === 0) return mid;
//     if (sum > 0) right = mid - 1;
//     if (sum < 0) left = mid + 1;
//   }

//   return index;
// }


