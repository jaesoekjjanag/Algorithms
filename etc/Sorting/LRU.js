//캐시에 있으면 찾아서 삭제 후 맨 앞으로 놓고
//캐시에 없으면 맨 앞에 추가 한 뒤 모두 한 칸씩 뒤로
function solution(s, n, arr) {
  let queue = [];
  for (let i of arr) {
    let temp;
    for (let j = queue.length - 1; j >= 0; j--) {
      //이전에 일치하는게 있었을 때 
      if (temp) queue[j + 1] = queue[j]

      //이번에 일치하면 temp에 저장해둠
      if (queue[j] === i) temp = queue[j];
    }
    if (temp) queue[0] = temp;
    else {
      if (queue.length === 5) queue.pop();
      queue.unshift(i);
    }
  }
  return queue
}

console.log(solution(5, 9, [1, 2, 3, 2, 6, 2, 3, 5, 7]))