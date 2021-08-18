#불연속 알파벳 체크

def check(word):
    visited = []
    done = []
    for i in word:
        if (i in done):
            return 0
        if (i not in visited):
            if(len(visited) != 0):
                done.append(visited[-1])
            visited.append(i)
    return 1
        
count = 0
for n in range(int(input())):
    count += check(input())

print(count)