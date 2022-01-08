function solution(n){
  //top-down 방식
  // if(n == 1)
  //   return 1;
  // if(n==2)
  //   return 2;
  // return solution(n-1) + solution(n-2);

  //bottom-up 방식
  arr = [0,1,2];
  if(n==1)
    return arr[1];
  if(n==2)
    return arr[2];
  for(i=3; i<=n; i++){
    arr.push(arr[i-1] + arr[i-2]);
    if(i==n)
      return arr[i];
  }
  
}

console.log(solution(7)) //21