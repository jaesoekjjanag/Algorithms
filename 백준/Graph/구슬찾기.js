const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./구슬찾기.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const [n, m] = input[0].split(" ").map((x) => +x);

const lighter = Array.from({ length: n + 1 }, () => []);
const heavier = Array.from({ length: n + 1 }, () => []);

for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(" ");
  lighter[a].push(b);
  heavier[b].push(a);
}

function dfs(x, arr, visited) {
  visited[x] = 1;

  if (arr[x].length === 0) return 1;

  let r = 0;
  for (let next of arr[x]) {
    if (!visited[next]) {
      r += dfs(next, arr, visited);
    }
  }

  return r + 1;
}

let answer = 0;
for (let i = 1; i <= n; i++) {
  const lighterCnt = dfs(i, lighter, Array(n + 1).fill(0));
  if (lighterCnt - 1 >= (n + 1) / 2) {
    answer += 1;
    continue;
  }
  const heavierCnt = dfs(i, heavier, Array(n + 1).fill(0));
  if (heavierCnt - 1 >= (n + 1) / 2) answer += 1;
}
console.log(answer);

// for (let i = 1; i <= m; i++) {
//   //a가 b보다 무거움
//   const [a, b] = input[i].split(" ");
//   graph[b][1].push(a);
//   graph[a][0].push(b);
// }

// for (let i = 1; i <= n; i++) {
//   if (graph[i][0].length > 0 || visited[i]) continue;

//   visited[i] = true;
//   dfs(i, 0);
// }

// function dfs(x, count) {
//   visited[x] = 1;
//   left[x] += count;

//   let r = 0;
//   if (graph[x][1]) {
//     for (let next of graph[x][1]) {
//       r += dfs(next, count + 1) + 1;
//     }
//   }

//   right[x] = r;
//   return r;
// }

// let answer = 0;

// for (let i = 1; i <= n; i++) {
//   if (left[i] >= (n + 1) / 2 || right[i] >= (n + 1) / 2) {
//     answer += 1;
//   }
// }

// console.log(answer);
