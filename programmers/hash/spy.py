from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer

# 무친코드.. 그냥 무턱대고 덤비지 말라는게 교훈. 


# def solution(clothes):
#     types = {}
#     for i in clothes:
#         types[i[0]] = i[1]
#     types_ctn = len(set(list(types.values())))
#     total_ctn = 0
#     total = 1
#     for i in range(1, types_ctn + 1):
#         print(i)
#         total *= i
#     total -= 1
#     return total
    # total_list = list(types.values())
    # for i in range(1, types_ctn):
    #     result = list(combinations(total_list, i))
    #     total_ctn += len(set(result))
    #     print(set(result))
    # return total_ctn + len(clothes)





# def solution(clothes):
#     types = {}
#     for i in clothes:
#         types[i[0]] = i[1]
#     types_ctn = len(set(list(types.values())))
#     total_ctn = 0
#     total_list = list(types.values())
#     for i in range(1, types_ctn):
#         result = list(combinations(total_list, i))
#         total_ctn += len(set(result))
#         print(set(result))
#     return total_ctn + len(clothes)






# def solution(clothes):
#     types = {}
#     for i in clothes:
#         if i[1] not in types:
#             types[i[1]] = []
#             types[i[1]].append(i[0])
#         else:
#             types[i[1]].append(i[0])
#     total_li = list(types.values())
#     total_com = list(product(total_li, repeat = 2))
#     print(total_com)
    # print(len(clothes))
    
    # cases = 0
    # for j in range(len(clothes)):
    #     for k in range(j)
    #     cases += len(list(combinations(types, j)))
    # return cases


# def solution(clothes):
#     types = {}
#     for i in clothes:
#         if i[1] not in types:
#             types[i[1]] = 1
#         else:
#             types[i[1]] += 1
#     cases = 0
#     if len(types.values()) > 1:
#         cases = 1
#         for j in types.values():
#             cases *= j
#     return len(clothes)





    # types = []
    # for i in clothes:
    #     if [i[1], 1] not in types:
    #         types.append([i[1], 1])
    #     else:
    #         idx = types.index([i[1], 1])
    #         types[idx][1] += 1
    # print(types)
    # return len(clothes)