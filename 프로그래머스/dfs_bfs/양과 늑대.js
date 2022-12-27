// 0: 양, 1: 늑대

function solution(info, edges) {
  var answer = 0;
  const graph = {};
  info.forEach((_, i) => (graph[i] = []));

  edges.forEach(([a, b]) => graph[a].push(b));

  const possible = [0]; //갈 수 있는 노드
  const dfs = (cur, sheep, wolf, possible) => {
    const animal = info[cur];
    if (animal === undefined) return;

    if (animal) {
      ++wolf;
    } else {
      ++sheep;
      answer = Math.max(answer, sheep);
    }

    if (wolf >= sheep) return;

    possible = possible.filter((n) => n !== cur);
    if (!graph[cur]) return;

    const [left, right] = graph[cur];
    if (left < info.length) possible.push(left);
    if (right < info.length) possible.push(right);

    possible.forEach((p) => dfs(p, sheep, wolf, possible));
  };

  dfs(0, 0, 0, possible);
  return answer;
}

console.log(
  solution(
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [
      [0, 1],
      [1, 2],
      [1, 4],
      [0, 8],
      [8, 7],
      [9, 10],
      [9, 11],
      [4, 3],
      [6, 5],
      [4, 6],
      [8, 9],
    ]
  )
);
