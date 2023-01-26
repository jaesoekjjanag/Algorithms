function solution(routes) {
  routes.sort((a, b) => a[1] - b[1]);
  let answer = 0;
  let camera = -30001;

  routes.forEach(([start, end]) => {
    if (camera < start) {
      camera = end;
      ++answer;
    }
  });

  return answer;
}
