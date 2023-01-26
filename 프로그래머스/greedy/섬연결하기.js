function getParent(parent, a) {
  if (parent[a] === a) return a;
  return getParent(parent, parent[a]);
}

function unionParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);
  if (a < b) parent[b] = a;
  else parent[a] = b;
}

function compareParent(parent, a, b) {
  a = getParent(parent, a);
  b = getParent(parent, b);
  if (a == b) return 1;
  return 0;
}

function solution(n, costs) {
  const parent = Array.from({ length: 100 }, (_, i) => i);

  let answer = 0;

  costs.sort((a, b) => a[2] - b[2]);
  costs.forEach(([a, b, cost]) => {
    if (compareParent(parent, a, b)) return;
    answer += cost;
    unionParent(parent, a, b);
  });

  console.log(parent);
  console.log(answer);
}

solution(7, [
  [2, 3, 7],
  [3, 6, 13],
  [3, 5, 23],
  [5, 6, 25],
  [0, 1, 29],
  [1, 5, 34],
  [1, 2, 35],
  [4, 5, 53],
  [0, 4, 75],
]);

// 7 [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]] 159
// 5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
// 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
// 4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
// 5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
// 6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
// 5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
// 5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
// 5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8
// 5 [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]] 7
// 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
// 4 [[0,1,1],[0,2,2],[2,3,1]] 4

// x:1, y:3
// function connect(x, y, array) {
//   array[x][y] = 1;
//   array[y][x] = 1;
// }

// function solution(n, costs) {
//   //from: [to, cost]
//   const nodes = Array.from({ length: 100 });
//   const graph = nodes.reduce((acc, _, i) => {
//     acc[i] = [];
//     return acc;
//   }, {});

//   costs.forEach(([a, b, cost]) => {
//     graph[a].push([b, cost]);
//     graph[b].push([a, cost]);
//   });

//   const connection = nodes.map(() => Array(100).fill(0));

//   let answer = 0;

//   for (let i in nodes) {
//     graph[i].sort((a, b) => a[1] - b[1]);
//     for (let [to, cost] of graph[i]) {
//       if (
//         isConnected(
//           i,
//           to,
//           connection,
//           Array.from({ length: 100 }, (_, j) => (j === i ? 1 : 0))
//         )
//       ) {
//         continue;
//       }
//       connect(i, to, connection);
//       answer += cost;
//       break;
//     }
//   }
//   return answer;
// }

// function isConnected(x, target, array, visited) {
//   if (array[x][target]) {
//     return true;
//   }

//   visited[target] = 1;

//   for (let i in array[x]) {
//     if (array[x][i] && !visited[i]) {
//       if (isConnected(target, i, array, visited)) return true;
//     }
//   }

//   return false;
// }

// 다익스트라 실패
// function solution(n, costs) {
//   const dist = Array.from({ length: 100 }, () => Infinity);
//   const visited = Array.from({ length: 100 }, () => 0);

//   const graph = dist.reduce((acc, _, i) => {
//     acc[i] = [];
//     return acc;
//   }, {});

//   costs.forEach(([a, b, cost]) => {
//     graph[a].push([b, cost]);
//     graph[b].push([a, cost]);
//   });

//   const q = [];

//   let visitCount = 0;
//   let crnt = 0;
//   dist[0] = 0;

//   while (visitCount < n) {
//     visited[crnt] = 1;
//     console.log(crnt, dist[crnt]);

//     for (let [dest, cost] of graph[crnt]) {
//       dist[dest] = Math.min(dist[dest], dist[crnt] + cost);
//     }

//     crnt = dist.filter((x) => !visited[x]).sort((a, b) => a[1] - b[1])[0];

//     ++visitCount;
//   }
// }
