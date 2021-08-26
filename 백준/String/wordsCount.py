# 단어 수 세기

s = input().split(' ')
words = [i for i in s if i != '']
print(len(words))