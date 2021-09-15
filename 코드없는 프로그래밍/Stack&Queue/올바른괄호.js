function solution(arg) {
  let stack = []
  for (i of arg) {
    if (i == '(') stack.push(i)
    if (i == ')') {
      if (stack[stack.length - 1] == '(') stack.pop()
    }
  }
  if (stack.length > 0) return 'NO'
  return 'YES'
}

console.log(solution('()(())()((()))'))
 // ( 이면 push
    // ) 이고, top이 (이면 pop
    // ) 이고, top이 )이거나 아무것도 없으면 return NO
    // 끝까지 돌았는데 length > 0이면 NO
    // 끝까지 돌고 length == 0이면 YES