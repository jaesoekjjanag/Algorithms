// function solution(n, paths, gates, summits) {
//   const graph = {};
//   for (let p of paths) {
//     const [i, j, w] = p;
//     graph[i] ? graph[i].push([j, w]) : (graph[i] = [[j, w]]);
//     graph[j] ? graph[j].push([i, w]) : (graph[j] = [[i, w]]);
//   }

//   const answers = new Set();
//   let minIntensity = Infinity;

//   const dfs = (cur, visited, max, answers) => {
//     if (summits.includes(cur)) {
//       minIntensity = max;
//       return answers.add([cur, max]);
//     }

//     let n, c, res;
//     for (let d of graph[cur]) {
//       [n, c] = d;
//       if (gates.includes(n) || visited.includes(n) || c > minIntensity)
//         continue;
//       visited.push(cur);
//       res = dfs(n, visited, Math.max(max, c), answers);
//       visited.pop();
//     }
//   };

//   for (let g of gates) {
//     dfs(g, [], 0, answers, minIntensity);
//   }

//   return [...answers].sort((a, b) => {
//     return a[0] - b[0];
//   })[0];
// }

function solution(n, paths, gates, summits) {
  const graph = {};
  for (let p of paths) {
    const [i, j, w] = p; //i: from, j: to
    graph[j] ? graph[j].push([i, w]) : (graph[j] = [[i, w]]);
    graph[i] ? graph[i].push([j, w]) : (graph[i] = [[j, w]]);
  }

  for (let s of summits) {
    graph[s] = [];
  }

  const intensities = Array(n + 1).fill(Infinity);

  Q = [];
  let node;

  for (let g of gates) {
    Q.push(g);
    intensities[g] = 0;
    const visited = Array(n + 1).fill(0);

    while (Q.length) {
      node = Q.shift();
      if (visited[node]) continue;
      visited[node] = 1;
      for (let [next, cost] of graph[node]) {
        if (visited[next]) continue;
        const max = Math.max(intensities[node], cost);
        if (intensities[next] > max) {
          intensities[next] = max;
        }
        Q.push(next);
      }
      Q.sort((a, b) => intensities[a] - intensities[b]);
    }
  }

  return summits
    .map((v) => [v, intensities[v]])
    .sort((a, b) => {
      if (a[1] === b[1]) {
        return a[0] - b[0];
      }
      return a[1] - b[1];
    })[0];
}

console.log(
  solution(
    6,
    [
      [1, 2, 3],
      [2, 3, 5],
      [2, 4, 2],
      [2, 5, 4],
      [3, 4, 4],
      [4, 5, 3],
      [4, 6, 1],
      [5, 6, 1],
    ],
    [1, 3],
    [5]
  )
);
