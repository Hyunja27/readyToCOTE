import statistics

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # mid = statistics.median(citations)
    # idx = citations.index(mid)

    for i in range(1, len(citations) + 1):
        tmp = 0
        tmp2 = 0
        for k in citations:
            if k >= i:
                tmp += 1
            if k <= i:
                tmp2 += 1
        if tmp2 <= i and tmp >= i:
            if answer < i:
                answer = i
            
    return answer



# import statistics

# def solution(citations):
#     answer = 0
#     citations.sort()
#     mid = statistics.median(citations)
#     idx = citations.index(mid)

#     for i in range(idx, len(citations)):
#         tmp = 1
#         for k in range(i + 1, len(citations)):
#             if citations[k] >= citations[i]:
#                 tmp += 1
#         if citations[i] <= tmp:
#             if answer < tmp:
#                 answer = tmp
#     return answer