class Heap {
  constructor(arr) {
    this.heap = [null];
    if (arr instanceof Array) {
      this.heap = this.heap.concat(arr);
      this.heapify();
    }

    this.rootIndex = 1;
  }

  left(index) {
    return index * 2;
  }

  right(index) {
    return index * 2 + 1;
  }

  parent(index) {
    return parseInt(index / 2);
  }

  heapPush(node) {
    this.heap.push(node);
    this.upHeap();
  }

  heapPop() {
    if (this.heap.length === 1) return;

    const { rootIndex } = this;
    [this.heap[rootIndex], this.heap[this.heap.length - 1]] = [
      this.heap[this.heap.length - 1],
      this.heap[rootIndex],
    ];

    const value = this.heap.pop();
    this.downHeap();
    return value;
  }

  upHeap() {
    let target = this.heap.length - 1;
    let parent = this.parent(target);

    while (target > 1 && this.heap[parent] > this.heap[target]) {
      [this.heap[target], this.heap[parent]] = [
        this.heap[parent],
        this.heap[target],
      ];
      target = parent;
      parent = this.parent(target);
    }
  }

  downHeap() {
    let target = this.rootIndex;
    let left = this.left(target);
    let right = this.right(target);

    while (
      this.heap[left] < this.heap[target] ||
      this.heap[right] < this.heap[target]
    ) {
      let min;
      if (this.heap[left] && this.heap[right]) {
        min = this.heap[left] < this.heap[right] ? left : right;
      } else {
        min = this.heap[left] ? left : right;
      }
      [this.heap[target], this.heap[min]] = [this.heap[min], this.heap[target]];
      target = min;
      left = this.left(target);
      right = this.right(target);
    }
  }

  heapify() {
    for (let i = this.heap.length - 1; i > 0; --i) {
      const left = this.left(i);
      const right = this.right(i);
      if (this.heap[right] || this.heap[left]) {
        let min;
        if (this.heap[left] && this.heap[right]) {
          min = this.heap[left] < this.heap[right] ? left : right;
        } else {
          min = this.heap[left] ? left : right;
        }
        if (this.heap[min] < this.heap[i]) {
          [this.heap[min], this.heap[i]] = [this.heap[i], this.heap[min]];
        }
      }
    }
  }
}

function solution(operations) {
  let h = new Heap();

  operations.forEach((operation) => {
    const [op, val] = operation.split(" ");
    if (op === "I") {
      h.heapPush(+val);
    }
    if (op === "D") {
      if (val === "1") {
        const temp = new Heap(h.heap.map((x) => -x).slice(1, h.heap.length));
        temp.heapPop();
        h = new Heap(temp.heap.map((x) => -x).slice(1, temp.heap.length));
      }
      if (val === "-1") {
        h.heapPop();
      }
    }
  });

  const answer = h.heap.slice(1, h.heap.length);

  return answer.length === 0
    ? [0, 0]
    : [Math.max.apply(null, answer), Math.min.apply(null, answer)];
}
