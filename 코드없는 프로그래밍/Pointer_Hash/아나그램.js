function anagram(a, b) {
  let obj = {}
  for (let i of a) {
    obj[i] ? obj[i] += 1 : obj[i] = 1
  }
  for (let j of b) {
    obj[j] -= 1
  }
  for (let k of Object.values(obj)) {
    if (k !== 0) return 'NO'
  }
  return 'YES'
}

console.log(anagram("AbaAeCe", "baeeACA"))

module.exports = anagram;