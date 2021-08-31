function solution(progresses, speeds) {
  let counts = []
  let count = 0

  while (progresses.length > 0) {
    //* 100이 되는 기능이 나올 떄까지 반복
    progresses = progresses.map((v, i) => v + speeds[i])
    //! head가 100 이상인지 확인
    if (progresses[0] >= 100) {
      //! 100 이상이면 shift 하고 다시 반복
      progresses.shift()
      count += 1
      if (progresses.length > 1) {
        for (let i of progresses) {
          if (i >= 100) {
            count += 1
          } else {
            for (let i = 1; i < count; i++) {
              progresses.shift()
            }
            counts.push(count)
            count = 0
          }
        }
      } else {
        counts.push(count)
      }
    }

  }

  return counts
}


console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))