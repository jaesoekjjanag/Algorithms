const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt'
const input = fs.readFileSync(filePath).toString().split('\n')

let condition = input[0]
let numbers = input[1]

solution(condition, numbers);

function solution(condition, numbers) {
  // N장의 카드 중 3장을 선택하여 M을 넘지 않으면서, 최대한 가깝게
  let N = condition.split(' ')[0]
  let M = condition.split(' ')[1]
  let numberArr = numbers.split(' ')

