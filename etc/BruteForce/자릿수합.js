//! 문자열로 바꾸어서 푸는 풀이
function solution(arr) {
  //max[0]에는 원본 숫자, max[1]에는 합친 숫자
  let max = [0, 0]
  for (let i = 0; i < arr.length; i++) {
    let sum = String(arr[i]).split('').reduce((a, b) => a + Number(b), 0)
    if (max[1] <= sum) {
      if (max[1] === sum && max[0] < sum) {
        //원래 값이 더 크면 아무것도 하지 않음
        continue
      }
      max[0] = arr[i]
      max[1] = sum
    }
  }
  console.log(max)
}

solution([128, 460, 603, 40, 521, 137, 123])

//! 몫과 나머지를 이용해 푸는 풀이
// function solution(n, arr){
//   let answer, max =0;
//   for(let x of arr){
//     let sum=0, tmp=x;
//     while(tmp){
//       sum += (tmp%10); //나머지
//       tmp=Math.floor(tmp/10); //몫
//     }
//     if(sum>max){
//       max = sum;
//       answer = x;
//     }else if(sum === max){
//       if(x>answer) answer =x;
//     }
//   }
//   return answer;
// }