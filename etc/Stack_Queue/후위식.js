function solution(str) {
  let op = ['+', '-', '*', '/']
  let stack = []

  for (let i of str) {
    if (op.includes(i)) {
      let a = +stack.pop()
      let b = +stack.pop()
      switch (i) {
        case '+':
          stack.push(a + b);
          break;
        case '-':
          stack.push(b - a);
          break;
        case '*':
          stack.push(a * b);
          break;
        case '/':
          stack.push(b / a);
          break;
        default:
          break;
      }
    } else { stack.push(i) }
  }
  return +stack[0]
}

console.log(solution('352+*9-'))