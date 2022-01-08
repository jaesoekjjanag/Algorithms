// function anagram(a, b) {
//   let obj = {}
//   for (let i of a) {
//     obj[i] ? obj[i] += 1 : obj[i] = 1
//   }
//   for (let j of b) {
//     obj[j] -= 1
//   }
//   for (let k of Object.values(obj)) {
//     if (k !== 0) return 'NO'
//   }
//   return 'YES'
// }

// function solution(S, T) {
//   let result = 0;
//   for (let i = 0; i < S.length; i++) {
//     ana = anagram(S.slice(i, i + T.length), T)
//     if (ana === 'YES') {
//       result++;
//     }
//   }
//   console.log(result)
// }

// solution('bacaAacba', 'abc')

function solution2(s, t) {
  let result = 0;
  let p1 = 0, p2 = t.length - 1;
  let window = {}, th = {}

  for (let i of s.slice(0, t.length - 1)) {
    window[i] ? window[i] += 1 : window[i] = 1;
  }

  for (let i of s.slice(0, t.length)) {
    th[i] ? th[i] += 1 : th[i] = 1;
  }
  console.log(th)
  for (p2; p2 < s.length; p2++) {
    window[s[p2]] ? window[s[p2]] += 1 : window[s[p2]] = 1;
    console.log(window)
    //* window와 t비교, 같으면?
    if (Object.entries(window).sort().toString() === Object.entries(th).sort().toString()) {
      result++
    }
    //* p1에 해당하는 값 window에서 drop하고 p1++
    window[s[p1]] -= 1;
    if (window[s[p1]] === 0) delete window[s[p1]];
    p1++
  }
  console.log(result)
}


console.log(solution2('bacaAacba', 'abc'))
