const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./거짓말.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const [n, m] = input[0].split(" ").map((x) => +x);
const noLie = new Set(
  input[1]
    .split(" ")
    .map((x) => +x)
    .slice(1)
);

const parent = Array.from({ length: n + 1 }, (_, i) => i);

const find = (x) => {
  if (parent[x] === x) return x;
  return find(parent[x]);
};

const union = (x, y) => {
  const xp = find(x);
  const yp = find(y);

  if (noLie.has(xp) && noLie.has(yp)) return;

  if (noLie.has(xp)) parent[yp] = xp;
  else if (noLie.has(yp)) parent[xp] = yp;
  else if (xp <= yp) parent[yp] = xp;
  else parent[xp] = yp;
};

for (let i = 2; i < m + 2; i++) {
  const participants = input[i].split(" ").slice(1);

  participants.reduce((prev, next) => {
    union(prev, next);
    return next;
  });
}

let answer = 0;
for (let i = 2; i < m + 2; i++) {
  const participants = input[i].split(" ").slice(1);
  answer += participants.every((p) => !noLie.has(find(p)));
}

console.log(answer);
