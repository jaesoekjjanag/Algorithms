function solution(result) {
  let stack = []
  let crnt = 0
  for (let i = 0; i < result.length; i++) {
    //숫자일 때,
    if (/\d/.test(result[i])) {
      if (result[i] == '1' && result[i + 1] == '0') {
        continue
      }
      stack.push(crnt)
      crnt = +result[i]
      if (result[i] == '0' && result[i - 1] == '1') {
        crnt = 10
      }
    }

    if (result[i] == 'D') crnt **= 2

    if (result[i] == 'T') crnt **= 3

    if (result[i] == '*') {
      crnt *= 2
      stack[stack.length - 1] *= 2
    }
    if (result[i] == '#') {
      crnt = -crnt
    }
    if (i == result.length - 1) {
      stack.push(crnt)
    }
  }
  return stack.reduce((a, b) => a + b)
}