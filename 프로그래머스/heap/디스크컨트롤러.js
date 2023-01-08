function solution(jobs) {
  let time = 0;
  let answer = 0;
  const { length } = jobs;
  jobs = jobs.sort((a, b) => a[0] - b[0]);

  while (jobs.length) {
    const availableJobs = jobs.filter((j) => j[0] <= time);
    if (availableJobs.length === 0) {
      time = jobs[0][0];
    } else {
      const task = availableJobs.sort((a, b) => a[1] - b[1])[0];
      const [req, proc] = task;

      answer += time - req + proc;
      time += proc;
      jobs = jobs.filter((j) => j !== task);
    }
  }

  return parseInt(answer / length);
}

console.log(
  solution([
    [0, 10],
    [2, 10],
    [25, 10],
    [25, 2],
  ])
);
