function solution(n){
  let d = [0,0];

  for(let i=2; i<n+1;i++ ){
    // 3개의 if문을 지나면서 네 가지 조건 중 가장 작은 값으로 update됨.
    d[i] = d[i-1] + 1;

    if(i%2 ==0){
      d[i] = Math.min(d[i], d[i/2] +1)
    }

    if(i%3 ==0){
      d[i] = Math.min(d[i], d[i/3] +1)
    }

    if(i%5 ==0){
      d[i] = Math.min(d[i], d[i/5] + 1)
    }
  }

  return d[n]
}

console.log(solution(26));
