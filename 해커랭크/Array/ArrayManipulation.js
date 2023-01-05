function arrayManipulation(n, queries) {
  const arr = Array(n + 1).fill(0);
  let result = 0;

  queries.forEach(([a, b, k], i) => {
    arr[a] += k;
    if (b < n) {
      arr[b + 1] += -k;
    }
  });

  arr.reduce((prev, cur) => {
    cur = prev + cur;
    result = Math.max(result, cur);
    return cur;
  });

  return result;
}

console.log(
  arrayManipulation(10, [
    [2, 6, 8],
    [3, 5, 7],
    [1, 8, 1],
    [5, 9, 15],
  ])
);

console.log(
  arrayManipulation(5, [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
  ])
);

console.log(
  arrayManipulation(4, [
    [2, 3, 603],
    [1, 1, 286],
    [4, 4, 882],
  ])
);
