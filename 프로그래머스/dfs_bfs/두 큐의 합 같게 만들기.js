const sum = (arr) => arr.reduce((a, b) => a + b, 0);

// 풀이1
function solution(queue1, queue2) {
  let q1Sum = sum(queue1);
  let q2Sum = sum(queue2);
  const SUM = q1Sum + q2Sum;
  const target = SUM / 2;

  let answer = 0;
  while (1) {
    if (q1Sum === SUM || q1Sum === 0) return -1;

    if (q1Sum < target) {
      const dq2 = queue2.shift();
      queue1.push(dq2);
      q1Sum += dq2;
    } else if (q1Sum > target) {
      const dq2 = queue1.shift();
      queue2.push(dq2);
      q1Sum -= dq2;
    } else {
      return answer;
    }

    answer++;
  }
}

// 풀이2
class Node {
  constructor(el) {
    this._el = el;
  }
  set next(next) {
    this._next = next;
  }
  get next() {
    return this._next;
  }
  set prev(prev) {
    this._prev = prev;
  }
  get prev() {
    return this._prev;
  }
  get el() {
    return _el;
  }
}
class Q {
  constructor(arr) {
    this.head = new Node(null);
    this.tail = new Node(null);
    let cur = this.head;

    for (let a of arr) {
      const newNode = new Node(a);
      cur.next = newNode;
      newNode.prev = cur;
      cur = newNode;
    }
    cur.next = this.tail;
  }

  dequeue() {
    const node = this.head;
    this.head.next = node.next;
    return node;
  }

  enqueue(node) {
    const last = this.tail.prev;
    last.next = node;
    node.prev = last;
    node.next = this.tail;
    this.tail.prev = node;
  }
}

// 풀이3
function solution(queue1, queue2) {
  const concated = [...queue1, ...queue2];
  const len = concated.length;
  const SUM = sum(concated);
  const target = SUM / 2;

  let q1Sum = sum(queue1);
  let left = 0;
  let right = queue1.length - 1;

  let answer = 0;
  while (1) {
    if (q1Sum === SUM || q1Sum === 0 || right >= len) return -1;

    if (q1Sum < target) {
      q1Sum += concated[++right];
    } else if (q1Sum > target) {
      q1Sum -= concated[left++];
    } else {
      return answer;
    }

    answer++;
  }
}
