function solution(citations) {
  let answer = citations.length;

  citations = citations.sort((a, b) => b - a);
  for (let c in citations) {
    if (+c >= citations[c]) {
      answer = +c;
      break;
    }
  }

  return answer;
}
