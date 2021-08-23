class Queue {
  constructor() {
    this.queue = []
  }
  push(val) {
    if (typeof (val) == 'number') {
      this.queue.push(val)
      return val
    }
  }
  pop() {
    if (this.queue.length == 0) {
      return -1
    }
    return this.queue.splice(0, 1)[0]
  }
  size() {
    return this.queue.length()
  }
  empty() {
    if (this.queue.length == 0) {
      return 1
    } else {
      return 0
    }
  }
  front() {
    if (this.queue[0]) {
      return this.queue[0]
    } else {
      return -1
    }
  }
  back() {
    if (this.queue[this.queue.length - 1]) {
      return this.queue[this.queue.length - 1]
    } else {
      return -1
    }
  }
}

const q1 = new Queue()
console.log(q1.push(10))
console.log(q1.push(5))
console.log(q1.front())
console.log(q1.back())
console.log(q1.pop())
console.log(q1.pop())
console.log(q1.empty())

