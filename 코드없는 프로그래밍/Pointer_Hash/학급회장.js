//* 자바스크립트 obj로 풀이
function solution(n, v) {
  let obj = {}
  Array.from(v).map(v => obj[v] ? obj[v] += 1 : obj[v] = 1)
  return Object.entries(obj).sort(([, a], [, b]) => b - a)[0][0]
}

console.log(solution(1, "BACBACCACCBDEDE"))

//* Map을 이용한 풀이.
function solution2(s) {
  let answer;
  let sH = new Map();
  for (let x of s) {
    if (sH.has(x)) sH.set(x, sH.get(x) + 1);
    else sH.set(x, 1);
  }
  let max = Number.MIN_SAFE_INTEGER;
  for (let [key, val] of sH) {
    if (val > max) {
      max = val;
      answer = key;
    }
  }
  return answer;
}

console.log(solution2('BACBACCACCBDEDE'))