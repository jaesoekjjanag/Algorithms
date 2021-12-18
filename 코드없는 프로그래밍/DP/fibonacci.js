function fib_naive(n){
  if (n==0){
    return 0;
  }else if(n ==1){
    return 1;
  }else{
    fib = fib_naive(n-1) + fib_naive(n-2);
    return fib;
  }
}

console.log(fib_naive(7));

//! 재귀적 DP를 이용한 방법(Top-Down 방식)
fib_arr = [0,1]
function fib_recur_dp(n){
  if(n< fib_arr.length){
    return fib_arr[n];
  }else{
    fib = fib_recur_dp(n-1) + fib_recur_dp(n-2);
    fib_arr.push(fib);
    return fib;
  }
}

console.log(fib_dp(7));

//! loop를 이용한 방법(Bottom-UP 방식)
function fib_dp(n){
  if (n==0){
    return 0;
  }else if(n ==1){
    return 1;
  }

  fib_arr = [0,1];

  for(let i=2; i <=n; i++){
    let num = fib_arr[i-1] + fib_arr[i-2]
    fib_arr.push(num);
  }
  return fib_arr[n]
}

console.log(fib_dp(7))