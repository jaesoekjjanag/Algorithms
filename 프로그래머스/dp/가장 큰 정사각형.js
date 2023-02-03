function solution(board) {
  let answer = Math.max(...board[0]);

  for (let i = 1; i < board.length; i++) {
    for (let j = 1; j < board[0].length; j++) {
      if (board[i][j]) {
        board[i][j] += Math.min(
          board[i - 1][j - 1],
          board[i - 1][j],
          board[i][j - 1]
        );
      }
      answer = Math.max(answer, board[i][j]);
    }
  }

  return answer ** 2;
}
