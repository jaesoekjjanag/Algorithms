function solution(rectangle, characterX, characterY, itemX, itemY) {
  let answer = 2500;
  const grid = Array.from({ length: 102 }, () => Array(102).fill(0));
  characterX *= 2;
  characterY *= 2;
  itemX *= 2;
  itemY *= 2;

  //! 테두리가 맞닿는 부분을 피하기 위해 간격을 2배로
  rectangle = rectangle.map((r) => r.map((x) => x * 2));

  rectangle.forEach(([x1, y1, x2, y2]) => {
    for (let i = x1; i <= x2; i++) {
      for (let j = y1; j <= y2; j++) {
        // 테두리이고, 다른 사각형의 내부가 아닌 경우
        if (i === x1 || i === x2 || j === y1 || j === y2) {
          if (grid[i][j] === 0) grid[i][j] = 1;
        } else {
          // 사각형의 내부
          grid[i][j] = -1;
        }
      }
    }
  });

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

  dfs(characterX, characterY, grid, 0);

  return answer / 2;
}
