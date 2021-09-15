function solution(board, moves) {
  let stack = []
  let count = 0
  for (let i of moves) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][i - 1] == 0) continue;
      if (stack[stack.length - 1] == board[j][i - 1]) {
        stack.pop()
        count += 2
      } else {
        stack.push(board[j][i - 1])
      }
      board[j][i - 1] = 0;
      break;
    }
  }
  return count
}

// console.log(solution([[0, 1, 0], [1, 2, 3], [3, 1, 2]], [2, 1, 3, 1, 2, 3, 3, 2]))

// console.log(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))

console.log(solution([[1, 1], [2, 3]], [1, 2, 1, 2]))
