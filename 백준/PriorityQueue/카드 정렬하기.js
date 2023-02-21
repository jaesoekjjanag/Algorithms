const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "./카드 정렬하기.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const heapq = (function heapq() {
  const ROOT_INDEX = 0;

  function getLeftIndex(index) {
    return (index + 1) * 2 - 1;
  }

  function getRightIndex(index) {
    return (index + 1) * 2;
  }

  function getParentIndex(index) {
    if (index <= 0) {
      return -1;
    }

    return Math.ceil(index / 2) - 1;
  }

  function hasValue(value) {
    if (value || value === 0) {
      return true;
    }

    return false;
  }

  function heappush(heap, node) {
    heap.push(node);
    upheap(heap);
  }

  function heappop(heap) {
    if (heap.length === 0) return;

    [heap[ROOT_INDEX], heap[heap.length - 1]] = [
      heap[heap.length - 1],
      heap[ROOT_INDEX],
    ];

    const value = heap.pop();
    downheap(heap);
    return value;
  }

  function upheap(arr) {
    let targetIndex = arr.length - 1;
    let parentIndex = getParentIndex(targetIndex);

    while (targetIndex > 0 && arr[parentIndex] > arr[targetIndex]) {
      [arr[targetIndex], arr[parentIndex]] = [
        arr[parentIndex],
        arr[targetIndex],
      ];
      targetIndex = parentIndex;
      parentIndex = getParentIndex(targetIndex);
    }
  }

  function downheap(arr) {
    let targetIndex = ROOT_INDEX;
    let leftIndex = getLeftIndex(targetIndex);
    let rightIndex = getRightIndex(targetIndex);

    while (
      arr[leftIndex] < arr[targetIndex] ||
      arr[rightIndex] < arr[targetIndex]
    ) {
      let minIndex;
      if (hasValue(arr[leftIndex]) && hasValue(arr[rightIndex])) {
        minIndex = arr[leftIndex] < arr[rightIndex] ? leftIndex : rightIndex;
      } else {
        minIndex = leftIndex ?? rightIndex;
      }

      [arr[targetIndex], arr[minIndex]] = [arr[minIndex], arr[targetIndex]];
      targetIndex = minIndex;
      leftIndex = getLeftIndex(targetIndex);
      rightIndex = getRightIndex(targetIndex);
    }
  }

  function heapify(arr) {
    for (let targetIndex = arr.length - 1; targetIndex >= 0; --targetIndex) {
      const leftIndex = getLeftIndex(targetIndex);
      const rightIndex = getRightIndex(targetIndex);

      const bothHasValue =
        hasValue(arr[leftIndex]) && hasValue(arr[rightIndex]);
      if (!bothHasValue) {
        continue;
      }

      let minIndex;
      if (hasValue(arr[leftIndex]) && hasValue(arr[rightIndex])) {
        minIndex = arr[leftIndex] < arr[rightIndex] ? leftIndex : rightIndex;
      } else {
        minIndex = leftIndex ?? rightIndex;
      }

      if (arr[minIndex] < arr[targetIndex]) {
        [arr[minIndex], arr[targetIndex]] = [arr[targetIndex], arr[minIndex]];
      }
    }
    return arr;
  }

  return { heappush, heappop, heapify };
})();

const { heapify, heappop, heappush } = heapq;

const nums = input.slice(1).map((x) => +x);

heapify(nums);

let answer = 0;
let sum;
while (nums.length >= 2) {
  sum = heappop(nums) + heappop(nums);
  answer += sum;
  heappush(nums, sum);
}

console.log(answer);
