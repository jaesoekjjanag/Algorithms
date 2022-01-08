function solution(arr){
  const size = arr.length;

  const dp = [1];
  
  for(i=1; i<size; i++){
    let crntValue, lastValue;
    let max = 0;

    for(j=i-1; j>=0; j--){
      crntValue = arr[i];
      lastValue = arr[j];
      
      if(crntValue > lastValue && dp[j] > max){
        max = dp[j];
      }
    }

    dp[i] = max +1;
  }

  return dp.reduce((prev, crnt)=>{
    if(prev > crnt){
      return prev;
    }else{
      return crnt;
    }
  })

}

console.log(solution([5,3,7,8,6,2,9,4]));