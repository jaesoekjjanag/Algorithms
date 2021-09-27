// stack으로 풀면 O(n) queue로 풀면 O(n2)
function solution(p, n) {
  // A B C
  n = n.split("")
  let stack = p.split("").reverse();
  for (let i = 0; i < n.length; i++) {
    if (n[i] === stack[stack.length - 1]) {
      stack.pop()
    }
  }
  return stack.length > 0 ? "NO" : "YES"
}

console.log(solution("CBA", "CBDAGE"))
console.log(solution("CBA", "CABGE"))