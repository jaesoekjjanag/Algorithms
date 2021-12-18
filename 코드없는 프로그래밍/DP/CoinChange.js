//? n원을 최소한의 동전으로 거슬러 주는 방법. 총 몇개의 동전이 필요한가?

function solution(coins, n){
  let arr = [0];
  for(let i=1; i<=n; i++){
    if(coins.includes(i)){
      arr.push(1)
    }else if(i < coins[0]){
      arr.push(0);
    }
    else{
      let min = Infinity;
      for(let coin of coins){
        let sub =  arr[i-coin]
        if(min > sub) {
          min = sub;
        }
      }
      arr.push(min+1);
    }
  }

  return arr[n];
}

console.log(solution([2, 3, 5, 6, 7], 11))