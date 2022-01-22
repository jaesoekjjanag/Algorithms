const fs = require("fs");

const data = fs.readFileSync("수찾기.txt", "utf-8").split("\r\n");

let [n, arr, m, target] = data;

arr = arr.split(" ").sort((a, b) => a - b);
sortedTarget = target.split(" ").sort((a, b) => a - b);

pa = 0;
pt = 0;

const include = [];

while (pa < n && pt < m) {
  if (arr[pa] == sortedTarget[pt]) {
    include.push(arr[pa]);
    pt++;
    pa++;
  } else if (arr[pa] > sortedTarget[pt]) {
    pt++;
  } else {
    pa++;
  }
}

pi = 0;
for (let i of target.split(" ")) {
  if (i == include[pi]) {
    console.log(1);
    pi++;
  } else {
    console.log(0);
  }
}
