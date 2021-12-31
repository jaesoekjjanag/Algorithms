function solution(priorities, location) {
  //FIFO, QUEUE
  //현재 요소보다 뒤에 더 중요한 요소가 있다면 현재 요소를 맨 뒤로
  let max = priorities.reduce((a, b) => a > b ? a : b)
  let counter = 0
  while (priorities.length > 0) {
    if (priorities[0] >= max) {
      priorities.shift()
      max = priorities.length > 0 && priorities.reduce((a, b) => a > b ? a : b)
      counter += 1
      location -= 1
      if (location == -1) return counter
    } else {
      priorities.push(priorities.shift())
      location -= 1
      if (location == -1) location += priorities.length
    }
  }
}