function solution(n, info) {
  var records = [];
  let max = 0;
  const range = Array(info.length)
    .fill(0)
    .map((i) => i);

  function dfs(index, record, arrowLeft) {
    if (index > 11) {
      return;
    }

    if (arrowLeft === 0) {
      let apeach = 0;
      let lion = 0;
      for (let i in range) {
        if (record[i] === "w") {
          lion += 10 - i;
        } else if (info[i] != 0) {
          apeach += 10 - i;
        }
      }
      if (apeach > lion) return;

      const gap = lion - apeach;

      if (gap > max) {
        max = gap;
        records = [record];
      } else if (gap === max) {
        records.push(record);
      }

      return;
    }

    const apeachHit = info[index];
    if (record.length >= 10 && arrowLeft <= apeachHit) {
      dfs(index + 1, record + "n", 0);
    }
    if (arrowLeft > apeachHit) {
      dfs(index + 1, record + "w", arrowLeft - (apeachHit + 1));
    }
    dfs(index + 1, record + "l", arrowLeft);
  }

  dfs(0, "", n);

  if (records.length === 0 || max === 0) {
    return [-1];
  }

  records.sort((a, b) => b.length - a.length);
  const r = records[0];
  let arrowLeft = n;
  const answer = [];
  for (let i in range) {
    if (r[i] == "w") {
      answer.push(info[i] + 1);
      arrowLeft -= info[i] + 1;
    } else if (r[i] == "n") {
      answer.push(arrowLeft);
    } else {
      answer.push(0);
    }
  }

  return answer;
}
