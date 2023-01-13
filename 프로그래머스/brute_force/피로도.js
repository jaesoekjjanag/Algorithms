function solution(k, dungeons) {
  let answer = 0;

  function play(d, tired, visited) {
    const lastTired = tired - dungeons[d][1];
    const newVisited = [...visited, d];

    answer = Math.max(answer, newVisited.length);

    for (let i in dungeons) {
      if (!newVisited.includes(i) && lastTired >= dungeons[i][0]) {
        play(i, lastTired, newVisited);
      }
    }
  }

  for (let i in dungeons) {
    play(i, k, []);
  }

  return answer;
}
