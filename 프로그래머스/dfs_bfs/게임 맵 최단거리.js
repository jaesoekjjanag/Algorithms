// 캐릭터: [0, 0]
// 상대 진영: [n-1, m-1]

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  const q = [[0, 0]];
  const d = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  while (q.length) {
    const [y, x] = q.shift();
    visited[y][x] = 1;

    const nextTasks = d.map(([dy, dx]) => [y + dy, x + dx]);
    nextTasks.forEach(([ny, nx]) => {
      if (
        ny >= 0 &&
        nx >= 0 &&
        ny < n &&
        nx < m &&
        maps[ny][nx] &&
        !visited[ny][nx]
      ) {
        maps[ny][nx] = maps[y][x] + 1;
        q.push([ny, nx]);
      }
    });
  }

  return maps[n - 1][m - 1] === 1 ? -1 : maps[n - 1][m - 1];
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
