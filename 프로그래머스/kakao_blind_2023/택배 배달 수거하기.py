def solution(cap, n, deliveries, pickups):
    answer = 0
    
    for p in range(n-1, -1, -1):
        if(deliveries[p] > 0 or pickups[p] > 0):
            answer += (p+1)
            deliver = 0
            for i in range(p, -1, -1):
                if(deliveries[i] > 0 and deliver < cap):
                    if(cap-deliver > deliveries[i]):
                        deliver += deliveries[i] 
                        deliveries[i] = 0
                    else:
                        deliveries[i] -= (cap-deliver)
                        deliver = cap
                
                if(deliver == cap): break
            
            pickup = 0
            for i in range(p, -1, -1):
                if(pickup == cap): break
                
                if(pickups[i] > 0 and pickup < cap):
                    if(cap-pickup > deliveries[i]):
                        pickup += pickups[i]
                        pickups[i] = 0
                    else:
                        pickups[i] -= (cap-pickup)
                        pickup = cap
                        
            print(pickup, deliver)                
                        
    
    return answer*2

solution()