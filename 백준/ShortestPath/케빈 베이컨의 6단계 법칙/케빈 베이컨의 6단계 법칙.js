const fs = require("fs");
const filePath =
  process.platform === "linux"
    ? "/dev/stdin"
    : "./케빈 베이컨의 6단계 법칙.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const [n, m] = input[0].split(" ").map((x) => +x);

const dist = Array.from({ length: n + 1 }, (_, i) =>
  Array.from({ length: n + 1 }, (_, j) => (i === j ? 0 : Infinity))
);

for (let i = 1; i <= m; i++) {
  const [a, b] = input[i].split(" ");
  dist[a][b] = 1;
  dist[b][a] = 1;
}

for (let k = 1; k <= n; k++) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
    }
  }
}

let min = Infinity;
let alter;

for (let i = 1; i <= n; i++) {
  const sum = dist[i].reduce((acc, x) => (x === Infinity ? acc : acc + x), 0);
  if (sum < min) {
    min = sum;
    alter = i;
  }
}

console.log(alter);
