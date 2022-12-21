function solution(fees, records) {
  const [defaultTime, defaultFee, unitTime, unitFee] = fees;

  const bills = {};
  const history = {};

  const calDiff = (inTime, outTime) => {
    const [inHour, inMinute] = inTime.split(":");
    const [outHour, outMinute] = outTime.split(":");

    return +outHour * 60 + +outMinute - (+inHour * 60 + +inMinute);
  };

  for (let r of records) {
    const [time, num, content] = r.split(" ");

    if (!history[num]) {
      history[num] = time;
    } else {
      const inTime = history[num];
      const diff = calDiff(inTime, time);
      bills[num] ? (bills[num] += diff) : (bills[num] = diff);
      delete history[num];
    }
  }

  for (let num in history) {
    const inTime = history[num];
    const outTime = "23:59";
    const diff = calDiff(inTime, outTime);
    bills[num] ? (bills[num] += diff) : (bills[num] = diff);
  }

  const answer = [];
  for (let num in bills) {
    const overTime = bills[num] - defaultTime;
    if (overTime < 0) {
      answer.push([num, defaultFee]);
    } else {
      answer.push([num, defaultFee + Math.ceil(overTime / unitTime) * unitFee]);
    }
  }

  answer.sort((a, b) => a[0] - b[0]);
  return answer.map((v) => v[1]);
}
