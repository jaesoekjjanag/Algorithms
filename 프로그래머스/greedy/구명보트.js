function solution(people, limit) {
  var answer = 0;
  people.sort((a, b) => b - a);
  const visited = Array(people.length).fill(0);

  let rightIndex = people.length - 1;
  for (let i in people) {
    if (visited[i]) break;

    let sum = people[i];
    while (sum + people[rightIndex] <= limit) {
      visited[rightIndex] = 1;
      sum += people[rightIndex];
      --rightIndex;
    }
    ++answer;
  }

  return answer;
}
