function solution(tickets) {
  const graph = tickets.reduce((acc, [from, to]) => {
    acc[from] ? acc[from].push(to) : (acc[from] = [to]);
    return acc;
  }, {});

  Object.keys(graph).forEach((key) => graph[key].sort());

  function dfs(from, path) {
    path.push(from);
    if (path.length == tickets.length + 1) {
      return path;
    }

    for (let i in graph[from]) {
      const to = graph[from].splice(i, 1)[0];

      if (dfs(to, path)) {
        return path;
      } else {
        path.pop();
        graph[from].splice(i, 0, to);
      }
    }

    return false;
  }

  return dfs("ICN", []);
}

console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
