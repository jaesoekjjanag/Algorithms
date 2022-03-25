n = int(input())

people = []
for _ in range(n):
  age, name = input().split()
  people.append([int(age), name])
  
for age, name in sorted(people, key=lambda x: x[0]):
  print(age, name)