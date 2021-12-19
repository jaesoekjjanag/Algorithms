function BFS(frame, start, visited, n, m){
  const queue = [];
  const startString = start.toString();
  let [xIdx, yIdx] = start;

  if(visited.has(startString) || frame[xIdx][yIdx] == 1)
    return

  count ++;
  visited.add(startString);
  queue.push(start);

  let crnt;
  while(queue.length > 0){
    crnt = queue.shift();
    [xIdx, yIdx] = crnt;

  for(let i=-1; i<=1; i++){
      for(let j=-1; j<=1; j++){
        const x = xIdx+i;
        const y = yIdx+j;

        if(x >= 0 && y >= 0 && x<=n-1 && y<=m-1){
            if(!visited.has([x,y].toString()) && frame[x][y] == 0 ){
            queue.push([x, y]);
            visited.add([x, y].toString());
          }
        }
      }
    }
    
  }
}

const visited = new Set();
let count =0;

function solution(n, m, frame){
  //! 인접 노드는 arr[i-1][j-1] ~ arr[i+1][j+1] 최대 8개
  //! 방문하지 않은 0을 만나면 count를 1 올리고, 주변 0을 모두 방문 처리
  //! 1을 만나면 스킵

  for(let i=0; i<n; i++){
    for(let j=0; j<m; j++){
      BFS(frame, [i,j], visited, n, m);
    }
  }
  
  return count;
}

const frame1 = [[0,0,1,1,0],
                [0,0,0,1,1],
                [1,1,1,1,1],
                [0,0,0,0,0]];
                
console.log(solution(4,5,frame1));