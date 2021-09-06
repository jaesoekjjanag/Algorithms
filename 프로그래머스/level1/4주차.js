function solution(table, languages, preference) {
  let scores = []
  for (let i of table) {
    i = i.split(' ')
    let job = i[0]
    let job_lan = i.slice(1)
    let score = 0
    for (let j = 0; j < languages.length; j++) {
      if (job_lan.includes(languages[j])) score += (5 - job_lan.indexOf(languages[j])) * preference[j]
    }
    scores.push([job, score])
  }
  scores.sort((a, b) => {
    if (a[1] > b[1]) return -1
  })
  return scores.filter((v) => v[1] == scores[0][1]).sort()[0][0]
}