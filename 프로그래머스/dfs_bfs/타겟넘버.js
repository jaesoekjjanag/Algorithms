let count = 0;

function dfs(numbers, pointer, target){
  if(pointer == numbers.length){
    if(numbers.reduce((a,b)=>a+b) == target)
    count ++;
  }else{
    const plus = [...numbers]
    const minus = [...numbers];
    minus[pointer++] *= -1;
    
    dfs(plus, pointer, target);
    dfs(minus, pointer, target);
  }
}

function solution(numbers, target){
  dfs(numbers, 0, target);
  return count;
}