function isOneLetterDiff(from, to) {
  let count = 0;
  for (let i in from) {
    if (from[i] !== to[i]) ++count;
  }
  return count === 1;
}

function solution(begin, target, words) {
  var answer = 50;

  function dfs(cword, count, visited) {
    if (cword === target) {
      answer = Math.min(count, answer);
      return;
    }

    visited.add(cword);
    for (let w of words) {
      if (isOneLetterDiff(cword, w) && !visited.has(w)) {
        dfs(w, count + 1, visited);
        visited.delete(w);
      }
    }
  }

  dfs(begin, 0, new Set());

  return answer < 50 ? answer : 0;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));
