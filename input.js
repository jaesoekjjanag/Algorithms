const fs = require('fs')
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt'
const input = fs.readFileSync(filePath).toString().split('\n')

const inputC = +input[0]
const inputTestCase = [];

for (let i = 1; i <= inputC; ++i) {
  const arr = input[i].split(' ').map(item => +item)
  const newArr = arr.slice(1)
  const testCase = {
    N: arr[0],
    arr: newArr
  };
  inputTestCase.push(testCase)
}

solution(inputC, inputTestCase);

function solution(C, testCase) {
  //알고리즘
}