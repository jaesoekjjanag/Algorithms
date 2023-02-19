const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./바이러스.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

let n = +input[0];
let m = +input[1];

let graph = {};

for (let i = 2; i < m + 2; i++) {
  let [a, b] = input[i].split(" ");
  graph[a] ? graph[a].push(b) : (graph[a] = [b]);
  graph[b] ? graph[b].push(a) : (graph[b] = [a]);
}

const q = [1];
const visited = Array(n + 1).fill(0);
visited[1] = "1";

let count = -1;

while (q.length) {
  const crnt = q.shift();
  count += 1;

  for (let nxt of graph[crnt]) {
    if (visited[nxt]) continue;
    visited[nxt] = 1;
    q.push(nxt);
  }
}

console.log(count);
