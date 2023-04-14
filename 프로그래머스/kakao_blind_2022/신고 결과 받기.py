# 여러 번 신고 가능. 같은 사람에 대한 신고는 1회로 처리
# k번 이상 신고되면 이용 정지.
# report: "a b": a가 b를 신고
# k가 넘는 신고 중 자신을 제외한 수

from collections import defaultdict

def solution(id_list, report, k):
    reported = defaultdict(set)
    history = defaultdict(set)
    bloked = set()
    
    for r in report:
        a, b = r.split()
        reported[a].add(b)
        history[b].add(a) 
        if(len(history[b]) >= k):
            bloked.add(b)
    
    answer = []
    for id in id_list:
        count = 0
        for b in bloked:
            if(b in reported[id]):
                count += 1
        answer.append(count)
    
    return answer