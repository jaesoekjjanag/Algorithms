// function solution(arr, m) {
//   let p1 = 0;
//   let cnt = 0;
//   let acc = 0;

//   for (let p2 = 0; p2 < arr.length; p2++) {
//     acc += arr[p2];
//     if (acc >= m) {
//       //* p1증가, p2감소
//       if (acc === m) {
//         cnt++;
//         console.log(acc + " 일치")
//       }
//       acc = -arr[p1] + arr[++p1] + -arr[p2] + arr[--p2]
//       if (acc === m) {
//         cnt++;
//         console.log(acc + " 일치")
//       }
//     } else {
//       console.log(acc + " 미만 ")
//       cnt++;
//     }
//   }
//   console.log(cnt)
// }

// solution([1, 3, 1, 2, 3], 5)

function solution(m, arr) {
  let answer = 0, sum = 0, lt = 0;
  for (let rt = 0; rt < arr.length; rt++) {
    sum += arr[rt];
    while (sum > m) {
      sum -= arr[lt++];
    }
    answer += (rt - lt + 1);
  }
  return answer;
}

console.log(solution(5, [1, 3, 1, 2, 3]))