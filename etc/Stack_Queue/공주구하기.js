// 가장 간단한 풀이
// 포인터로 현재 위치를 기록. 해당 index를 splice한 뒤에 포인터 초기화

//스택, 큐의 개념을 활용한 풀이
//배열을 순회하면서, 맨 뒤로 이동 시킴.

// 연결리스트로 풀면 어떨까

function solution(n, k) {
  let q = Array(n).fill(0).map((v, i) => i + 1);
  while (q.length > 1) {
    for (let i = 1; i < k; i++) {
      q.push(q.shift());
    }
    q.shift()
  }
  return q[0]
}

console.log(solution(8, 3))