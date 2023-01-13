function solution(n, wires) {
  var answer = n;

  const graph = Array.from({ length: n }, (_, i) => i + 1).reduce((acc, x) => {
    acc[x] = [];
    return acc;
  }, {});

  wires.forEach(([a, b]) => {
    graph[a].push(b);
    graph[b].push(a);
  });

  function dfs(node, visited) {
    visited.push(node);

    for (let n of graph[node]) {
      if (!visited.includes(n)) {
        dfs(n, visited);
      }
    }

    return visited.length;
  }

  for (let w of wires) {
    const [a, b] = w;
    const left = dfs(a, [a, b]);
    const right = dfs(b, [a, b]);
    answer = Math.min(answer, Math.abs(left - right));
  }

  return answer;
}
