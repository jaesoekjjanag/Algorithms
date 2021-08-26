function solution(phone_number) {
  const arr = String(phone_number).split('')
  const slength = arr.length - 4
  const lfour = arr.splice(slength, 4)
  const result = Array(slength).fill('*').concat(lfour).join('')
  return result
}