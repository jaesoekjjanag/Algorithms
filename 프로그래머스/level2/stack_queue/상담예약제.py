from collections import deque

def solution(booked, unbooked):
  booked = deque(booked)
  unbooked = deque(unbooked)
  
  order = []
  crnt = min(booked[0][0], unbooked[0][0])
  
  def increment(time):
    if time[3:] >= "50":
      return str(format(int(time[:2]) + 1, '02')) + ":" + str(format(int(time[3:]) - 50, '02'))
    else:
      return str(time[:3] + str(format(int(time[3:]) + 10, '02')))
  
  while(booked or unbooked):
    if booked and crnt >= booked[0][0]:
        order.append(booked.popleft()[1])
        crnt = increment(crnt)
        continue
    elif unbooked and crnt >= unbooked[0][0]:
        order.append(unbooked.popleft()[1])
        crnt = increment(crnt)
        continue
    else:
      if booked and unbooked:
        crnt = min(booked[0][0], unbooked[0][0])
      elif not booked:
        crnt = unbooked[0][0]
      elif not unbooked:
        crnt = booked[0][0]

  return order


booked1 = [["09:10", "lee"]]
unbooked1 = [["09:00", "kim"], ["09:05", "bae"]]

booked2 = [["09:55", "hea"], ["10:05", "jee"]]
unbooked2 = [["10:04", "hee"], ["14:07", "eom"]]

booked3 = [["09:00", "김"], ["09:05", "박"], ["09:27", "성"]]
unbooked3 = [["09:01", "나"], ["09:10", "이"], ["09:35", "정"]]

print(solution(booked1, unbooked1))
print(solution(booked2, unbooked2))
print(solution(booked3, unbooked3))
