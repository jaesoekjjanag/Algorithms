# 여러번의 거래로 낼 수 있는 최대 이익
price = [7, 1, 5, 3, 6, 4]

result = 0
for i in range(1, len(price)):
  if price[i] > price[i-1]:
    result += price[i] - price[i-1]
    
print(result)