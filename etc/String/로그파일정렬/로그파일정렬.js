function logSort(arr) {
  const letters = [];
  const digits = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i].split(" ")[1].match("[0-9]")) {
      digits.push(arr[i]);
    } else {
      letters.push(arr[i]);
    }
  }

  letters.sort((a, b) => {
    aLogs = a.substr(a.indexOf(" ") + 1);
    bLogs = b.substr(b.indexOf(" ") + 1);
    if (aLogs == bLogs) {
      //로그가 같은 경우 식별자를 기준으로 정렬
      return a.localeCompare(b);
    } else {
      return aLogs.localeCompare(bLogs);
    }
  });
  console.log(letters.concat(digits));
}

logSort([
  "dig1 8 1 5 1",
  "let1 art can",
  "dig2 3 6",
  "let2 own kit dig",
  "let3 art zero",
]);
