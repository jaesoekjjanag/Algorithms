function solution(arr) {
  let children = []
  for (let i = 0; i < arr.length; i++) {
    if (!children[0] && arr[i] >= arr[i + 1]) {
      children.push(i + 1)
    }
    if (i > children[0] && arr[i] < arr[i - 1]) {
      children.push(i + 1)
    }
  }
  console.log(children[0], children[1])
}

solution([120, 125, 152, 130, 135, 135, 143, 127, 160])
solution([120, 130, 150, 150, 130, 150])