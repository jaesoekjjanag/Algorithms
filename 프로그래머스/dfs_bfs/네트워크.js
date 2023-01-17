function dfs(i, computers, visited) {
  if (visited[i]) return 0;

  visited[i] = 1;
  for (let j in computers[i]) {
    if (computers[i][j]) {
      dfs(j, computers, visited);
    }
  }

  return 1;
}

function solution(n, computers) {
  const visited = Array(n).fill(0);
  let answer = 0;

  for (let i in computers[0]) {
    answer += dfs(i, computers, visited);
  }

  return answer;
}
