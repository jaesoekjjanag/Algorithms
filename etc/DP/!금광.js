function solution(n, m, arr){
  //* 0~n-1, n~2n-1 ... n*m-1
  let table = []
  for(let i=0; i<n; i++){
    table.push(arr.slice(4*i, 4+4*i))
  }

  let dp = [...table]

  for(let i=0; i<n; i++){
    for(let j=1; j<m; j++){
      if(i == 0){
        dp[i][j] = dp[i][j] + Math.max(dp[i][j-1] , dp[i+1][j-1]);
      }
      if(i == 1){
        dp[i][j] = dp[i][j] + Math.max(dp[i-1][j-1], dp[i][j-1] , dp[i+1][j-1]);
      }
      if(i == 2){
        dp[i][j] = dp[i][j] + Math.max(dp[i-1][j-1], dp[i][j-1]);
      }
    }
  }
  
  let result = 0;
  for(let i=0; i<n; i++){
    if(dp[i][m-1] > result) result = dp[i][m-1];
  }
  console.log(result)
} 

solution(3, 4, [1,3,3,2,2,1,4,1,0,6,4,7])

