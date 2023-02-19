const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./숨바꼭질.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const graph = {};

for (let nodes of input.slice(1)) {
  let [a, b] = nodes.split(" ");
  graph[a] ? graph[a].push(b) : (graph[a] = [b]);
  graph[b] ? graph[b].push(a) : (graph[b] = [a]);
}

const q = [1];
const visited = Array(Object.keys(graph).length + 1).fill(0);
const distance = [...visited];

visited[1] = 1;
let max = 0;
while (q.length) {
  const crnt = q.shift();

  for (let next of graph[crnt]) {
    if (visited[next]) continue;

    visited[next] = 1;
    distance[next] = distance[crnt] + 1;
    max = Math.max(distance[next], max);
    q.push(next);
  }
}

const alters = distance.reduce((acc, x, i) => {
  if (x === max) {
    acc.push(i);
  }
  return acc;
}, []);

console.log(alters[0], max, alters.length);
