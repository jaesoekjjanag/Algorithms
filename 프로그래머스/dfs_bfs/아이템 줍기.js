function drawLine(start, end, grid) {
  const q = [start];
  const [sx, sy] = start;
  const [ex, ey] = end;

  const d = [
    [1, 0],
    [0, 1],
  ];
  const visited = Array.from({ length: 51 }, () => Array(51).fill(0));
  while (q.length) {
    const [x, y] = q.shift();
    visited[x][y] = 1;

    // 1: 모서리, 2: 내부.
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

      if (nx <= ex && ny <= ey && !visited[nx][ny]) {
        q.push([nx, ny]);
      }
    });
  }
}

function solution(rectangle, characterX, characterY, itemX, itemY) {
  let answer = 2500;
  const grid = Array.from({ length: 51 }, () => Array(51).fill(0));

  rectangle.forEach(([x1, y1, x2, y2]) => {
    drawLine([x1, y1], [x2, y2], grid);
  });

  const directions = {
    down: [0, -1],
    left: [-1, 0],
    right: [1, 0],
    up: [0, 1],
  };

  const priority = {
    down: 2,
    left: 1,
    right: 1,
    up: 0,
  };

  function dfs(x, y, grid, acc) {
    console.log(x, y);
    if (x === itemX && y === itemY) {
      answer = Math.min(answer, acc);
      return;
    }

    grid[x][y] = acc;

    const dup = [];
    Object.entries(directions).forEach(([dir, [dx, dy]]) => {
      if (
        !(x + dx === characterX && y + dy === characterY) &&
        grid[x + dx][y + dy] == 1
      ) {
        dup.push(dir);
      }
    });
    if (dup.length === 0) return;
    const direction = dup.sort((a, b) => priority[b] - priority[a])[0];

    const [dx, dy] = directions[direction];

    dfs(x + dx, y + dy, grid, acc + 1);
  }

  for (let d of Object.values(directions)) {
    const [dx, dy] = d;

    if (grid[characterX + dx][characterY + dy] === 1) {
      console.log();
      dfs(characterX + dx, characterY + dy, grid, 2);
    }
  }

  return answer - 1;
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
// console.log(
//   solution(
//     [
//       [1, 1, 7, 4],
//       [3, 2, 5, 5],
//       [4, 3, 6, 9],
//       [2, 6, 8, 8],
//     ],
//     1,
//     3,
//     7,
//     8
//   )
// );
