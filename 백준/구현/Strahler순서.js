const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./Strahler순서.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let testCaseNum = +input[0];
let cursor = 1;

for (testCaseNum; testCaseNum > 0; testCaseNum--) {
  [k, m, p] = input[cursor++].split(" ");
  const lines = [];

  for (let i = 0; i < p; ++i) {
    [a, b] = input[cursor++].split(" "); // a->b로 물이 흐름
    lines.push([+a, +b]);
  }
  solution(k, m, p, lines);
}

function solution(k, m, p, lines) {
  const graph = {}; //내가 향하는 노드, 나에게로 오는 노드
  Array(+m + 1)
    .fill(0)
    .forEach((_, i) => (graph[i] = [[], []]));

  const counts = Array(+m + 1).fill(0);
  const orders = Array(+m + 1).fill(1);

  for (let i = 0; i < p; ++i) {
    const [a, b] = lines[i];
    graph[a][0].push(b);
    graph[b][1].push(a);

    ++counts[b];
  }

  Q = [];

  for (let i = 1; i <= p; ++i) {
    if (counts[i] === 0) {
      Q.push(i);
    }
  }

  let cur;
  while (Q.length) {
    cur = Q.shift();
    // 나한테 오는 강물 중 가장 큰 값의 개수세기

    const maxOrder = graph[cur][1].length
      ? graph[cur][1].reduce((a, b) => {
          return Math.max(a, orders[b]);
        }, orders[a])
      : 1;

    const maxCount = graph[cur][1].filter((v) => orders[v] === maxOrder).length;
    orders[cur] = maxCount >= 2 ? maxOrder + 1 : maxOrder;

    for (let next of graph[cur][0]) {
      --counts[next];
      if (counts[next] === 0 && graph[next]) {
        Q.push(next);
      }
    }
  }

  console.log(k, orders[m]);
}
