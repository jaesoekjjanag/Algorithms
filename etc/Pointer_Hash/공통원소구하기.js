function solution(A, B) {
  let arr = []
  A.sort((a, b) => a - b)
  B.sort((a, b) => a - b)

  pA = 0;
  pB = 0;

  for (pA; pA < A.length; pA++) {
    if (A[pA] === B[pB]) {
      arr.push(A[pA])
      pB++
    } else {
      if (B[pB] < A[pA]) pB++;
    }
  }
  return arr.join(" ")
}

console.log(solution([1, 3, 9, 5, 2], [3, 2, 5, 7, 8]))