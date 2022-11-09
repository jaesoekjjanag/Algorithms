from collections import deque

def solution(bridge_length, weight_limit, truck_weights):
    # bridge_length는 트럭이 동시에 올라갈 수 있는 수 임과 동시에
    # 한 대의 트럭이 다리를 모두 건너는데 소요되는 시간
    length = len(truck_weights)
    
    time = 0
    
    q = deque(truck_weights)
    
    truck_done = []
    truck_running = deque([])
    
    weight = 0
    
    while True:
        if(truck_running and time - truck_running[0][1] + 1 == bridge_length):
            done = truck_running.popleft()
            weight -= done[0]
            truck_done.append(done[0])
        
        time += 1
        
        if(len(truck_done) == length):
            return time
        
        if(len(truck_running) == bridge_length):
            continue
        
        if(q and q[0] + weight > weight_limit):
            continue
        
        if(q):
            crnt_truck = q.popleft()
            weight += crnt_truck
            truck_running.append([crnt_truck, time])
    
        
solution(100, 100, [10])