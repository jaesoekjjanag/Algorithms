function solution(arr){
  let table = []
  table.push(arr[0]);
  table.push(Math.max(arr[0], arr[1]));

  for(let i=2; i<arr.length; i++){
    let x = arr[i];
    table.push(Math.max(table[i-2] + x, table[i-1]));
  }

  return table[table.length-1];
}

console.log(solution([1,3,1,5]));