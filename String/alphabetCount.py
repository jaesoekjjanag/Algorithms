## 알파벳 숫자 세기
key = []
value = []
s = input()
for i in s.lower():
    if(i in key):
        value[key.index(i)] += 1
    else:
        key.append(i)
        value.append(1)
mVal = []
for j in value:
    if j == max(value):
        mVal.append(j)
if len(mVal) > 1:
    print('?')
else:
    print(key[value.index(mVal[0])].upper())