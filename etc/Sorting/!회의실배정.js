function solution(n, arr){
  let count =0;
  let reservations =[]

  while(arr.length > 0){
    //회의 시간이 가장 짧은 순
    arr.sort((a,b)=>{
      const subA = a[1]-a[0];
      const subB = b[1]-b[0];
      
    return subB-subA
  })

  
  reservations.push(arr.pop());
  count ++;
  arr = arr.filter((el)=>el[0] >= reservations[reservations.length-1][1]);

  arr.sort((a, b)=>{
    const subA = reservations[reservations.length-1][1] - a[0]
    const subB = reservations[reservations.length-1][1] - b[0]

    return subA - subB;
  })
}
  console.log(count);
  console.log(reservations);
}

solution(5, [[1,4],[2,3],[3,5],[4,6],[5,7]])
solution(3, [[3,3],[1,3],[2,3]])