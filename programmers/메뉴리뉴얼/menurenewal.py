import itertools
from collections import Counter

# data = dict()

# 코스를 길이로 역정렬(제일 긴 것이 맨 앞에)
    
# i 맨 앞 코스요소의 길이만큼 for:
#     tmpList = []
#     j 코스 개수만큼 for:
#         tmpList.append(코스[j] 콤비네이션 (i개 조합))
#     k tmplist만큼 for:
#         k 길이만큼 for:
#             data[k] += 1
            

def solution(orders, course):
    
    data = dict()
    tmpList = []
    rt = []
    
    orders.sort(key=len, reverse=True)
    for i in range(0,max(course) + 1):
        if i not in course:
            pass
        else:
            for j in orders:
                tmp = list(itertools.combinations(list(j),i))
                for k in tmp:
                    m = sorted(list(k))
                    tmpList.append(''.join(m))
    counting = dict(Counter(tmpList))
    counting = sorted(counting.items(), key=lambda x:x[1], reverse=True)

    for i in course:
        same = 0
        for j in counting:
            if len(j[0]) == i and same == 0 and j[1] > 1:
                rt.append(j[0])
                same = j[1]
            elif len(j[0]) == i and same == j[1] and j[1] > 1:
                rt.append(j[0])
            elif len(j[0]) != i:
                pass
    rt.sort()
    return(rt)