function solution(str) {
  let stack = []
  for (let i of str) {
    if (i == ')') {
      while (true) {
        if (stack[stack.length - 1] == '(') {
          stack.pop()
          break
        }
        stack.pop()
      }
    } else {
      stack.push(i)
    }
  }
  return stack.join('')
}

console.log(solution('(A(BC)D)EF(G(H)(IJ)K)LM(N)'))