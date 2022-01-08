function solution(n, arr){
  arr = arr.sort((a,b)=>a[1]-b[1]);

  dp = [0];

  for(let i=1; i<=n; i++){
    if(i < arr[0][1]){
      dp.push(0);
    }else{
      let max = dp[dp.length-1];
      arr.forEach((v)=>{
        if(v[1] == i && v[0] > max)
          max = v[0];
      })
      let time;
      for(let j=0; j<arr.length; j++){
        time = arr[j][1];
        if(i > time){
          if(dp[i-time] + dp[time]> max && (i-time) > time)
          max = dp[i-time] + dp[time];
        }
      }
      dp.push(max);
    }
  }

  return dp[n];
}

console.log(solution(20, [[6,3],[7,4],[10,5],[15,8],[25,12]]))