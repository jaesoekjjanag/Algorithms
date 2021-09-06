function solution(n, arr1, arr2) {
  //벽은 or, 공백은 and 조건
  //배열의 요소를 2진수로 바꾼 뒤 서로 비교
  let result = []
  for (let i = 0; i < arr1.length; i++) {
    result.push((arr1[i] | arr2[i]).toString(2).padStart(n, 0).replace(/1/g, '#').replace(/0/g, ' '))
  }
  return result
}