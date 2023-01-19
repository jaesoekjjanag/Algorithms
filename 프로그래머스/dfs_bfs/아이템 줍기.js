function drawLine(start, end, grid) {
  const q = [start];
  const [sx, sy] = start;
  const [ex, ey] = end;

  const d = [
    [1, 0],
    [0, 1],
  ];
  const visited = Array.from({ length: 102 }, () => Array(102).fill(0));
  while (q.length) {
    const [x, y] = q.shift();
    visited[x][y] = 1;
    // 1: 모서리, -1: 내부.
    // 모서리지만 이미 2로 채워져 있다는 것은 다른 도형의 내부라는 뜻. 모서리 초리하지 않는다.
    if (x === sx || x === ex || y === sy || y === ey) {
      if (grid[x][y] !== -1) {
        grid[x][y] = 1;
      }
    } else {
      grid[x][y] = -1;
    }

    d.forEach(([dx, dy]) => {
      const [nx, ny] = [x + dx, y + dy];
      if (nx <= ex && ny <= ey && visited[nx][ny] === 0) {
        q.push([nx, ny]);
      }
    });
  }
}

function solution(rectangle, characterX, characterY, itemX, itemY) {
  let answer = 2500;
  const grid = Array.from({ length: 102 }, () => Array(102).fill(0));
  characterX *= 2;
  characterY *= 2;
  itemX *= 2;
  itemY *= 2;

  rectangle = rectangle.map((r) => r.map((x) => x * 2));

  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let i = x1; i <= x2; i++) {
      for (let j = y1; j <= y2; j++) {
        if (i === x1 || i === x2 || j === y1 || j === y2) {
          if (grid[i][j] === 0) grid[i][j] = 1;
        } else {
          grid[i][j] = -1;
        }
      }
    }
  });

  // for (let i = 30; i > 0; i--) {
  //   for (let j = 1; j <= 30; j++) {
  //     if (grid[i][j] === 1) {
  //       process.stdout.write("*");
  //     } else {
  //       process.stdout.write(" ");
  //     }
  //   }
  //   console.log();
  // }

  const directions = [
    [0, -1],
    [-1, 0],
    [1, 0],
    [0, 1],
  ];

  function dfs(x, y, grid, acc) {
    if (x === itemX && y === itemY) {
      answer = Math.min(answer, acc);
      return;
    }

    grid[x][y] = 0;
    for (let [dx, dy] of directions) {
      const [nx, ny] = [x + dx, y + dy];
      if (grid[nx][ny] === 1) {
        dfs(x + dx, y + dy, grid, acc + 1);
      }
    }
  }

  dfs(characterX, characterY, grid, 1);

  return (answer - 1) / 2;
}

console.log(
  solution(
    [
      [1, 1, 8, 4],
      [2, 2, 4, 9],
      [3, 6, 9, 8],
      [6, 3, 7, 7],
    ],
    9,
    7,
    6,
    1
  )
);
console.log(
  solution(
    [
      [1, 1, 7, 4],
      [3, 2, 5, 5],
      [4, 3, 6, 9],
      [2, 6, 8, 8],
    ],
    1,
    3,
    7,
    8
  )
);
console.log(solution([[1, 1, 5, 7]], 1, 1, 4, 7));
