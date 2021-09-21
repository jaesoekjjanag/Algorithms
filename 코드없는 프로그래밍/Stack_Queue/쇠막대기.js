// ()는 레이저
// (())는 쇠막대기를 레이저로 절단한 것  ((())())

function solution(str) {
  let stack = []
  let sum = 0

  for (let i = 0; i < str.length; i++) {
    if (str[i] === ')') {
      if (str[i - 1] === '(') {
        //레이저
        stack.pop()
        stack = stack.map(v => v + 1)
      } else {
        // 파이프 끝
        sum += stack.pop()
      }
    } else {
      // (가 들어오면 push
      stack.push(1)
    }
  }
  return sum
}

// solution('((())())')
console.log(solution('()(((()())(())()))(())'))
