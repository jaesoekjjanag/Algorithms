function solution(participant, completion) {
  let obj = {}
  participant.map(v => obj[v] ? obj[v]++ : obj[v] = 1)
  completion.map(v => obj[v]--)
  return Object.keys(obj).filter(v => obj[v] > 0)[0]
}