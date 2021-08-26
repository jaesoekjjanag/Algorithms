function solution(progresses, speeds) {
  //progresses: [93,30,55] FIFO
  let counts = []

  counts.push(work(progresses, speeds))
  return counts
}

function work(progresses, speeds) {
  let len = progresses.length
  let count = 0

  while (true) {
    //* 100이 되는 기능이 나올 떄까지 반복
    progresses = progresses.map((v, i) => v + speeds[i])
    // //! head가 100 이상인지 확인
    // if (progresses[0] >= 100) {
    //   //! 100 이상이면 shift 하고 다시 반복
    //   progresses.shift()
    //   count += 1
    //   console.log(progresses)
    // }

  }
}

// console.log(solution([93, 30, 55], [1, 30, 5]))
work([93, 30, 55], [1, 30, 5])