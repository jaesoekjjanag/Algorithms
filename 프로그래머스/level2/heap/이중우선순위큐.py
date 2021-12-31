import heapq

def insert(q, n):
    heapq.heappush(q, int(n))

def deleteMax(q):
    for i in range(len(q)):
        q[i] *= -1
    heapq.heapify(q)
    
    max = heapq.heappop(q)
    for i in range(len(q)):
        q[i] *= -1
    heapq.heapify(q)
    return -max
    
def deleteMin(q):
    min = heapq.heappop(q)
    return min
    
def solution(operations):
    queue = []
    
    for operation in operations:
        op, num = operation.split()
        if(op == 'I'):
            insert(queue, num)
        elif (op == 'D' and len(queue) > 0):
            if(num == '1'):
                deleteMax(queue)
            if(num == '-1'):
                deleteMin(queue)
    if(len(queue) == 0):
        return [0,0]
    
    else:
        return [deleteMax(queue), deleteMin(queue)]