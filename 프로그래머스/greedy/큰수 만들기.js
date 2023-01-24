// 실패
function solution1(number, k) {
  let answer = [number[0]];
  const length = number.length - k;

  for (let n of [...number].slice(1)) {
    let flag = false;
    for (let i in answer) {
      if (k === 0) break;
      if (answer[i] < n && k >= answer.length - i) {
        flag = true;
        answer[i] = n;
        k -= answer.length - i;
        answer.splice(i + 1);
        break;
      }
    }
    if (!flag) {
      answer.push(n);
    }
  }

  return answer.slice(0, length).join("");
}

function solution2(number, k) {
  const length = number.length - k;
  let answer = [];

  for (let n of number) {
    while (k > 0 && answer.length && answer[answer.length - 1] < n) {
      answer.pop();
      k -= 1;
    }
    answer.push(n);
  }

  return answer.slice(0, length).join("");
}
