function solution(a, b) {
  days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
  //date 메소드는 월이 0부터 시작
  return days[new Date(2016, a - 1, b)]
}