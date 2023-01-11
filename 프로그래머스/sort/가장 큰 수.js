function solution(numbers) {
  const answer = numbers
    .map((x) => "" + x)
    .sort((a, b) => b + a - (a + b))
    .reduce((a, b) => a + b);
  return answer[0] === "0" ? "0" : answer;
}
