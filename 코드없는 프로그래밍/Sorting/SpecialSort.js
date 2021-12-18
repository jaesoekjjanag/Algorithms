function solution(arr) {
  let m = [];
  let p = [];
  for (let i of arr) {
    if (i < 0) m.push(i);
    else p.push(i);
  }
  return m.concat(p).join(" ")
}

console.log(solution([1, 2, 3, -3, -2, 5, 6, -6]))