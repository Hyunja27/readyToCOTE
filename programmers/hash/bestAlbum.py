
def solution(genres, plays):
    answer = []
    playsBygenres = [0] * len(set(genres))
    totalList = []

    for i in range(len(genres)):
        totalList.append([genres[i], plays[i], i])
    totalList.sort()
    j = 0
    for i in totalList:
        if playsBygenres[j] == 0:
            playsBygenres[j] = [i[0], i[1], 1]
        else:
            if playsBygenres[j][0] == i[0]:
                playsBygenres[j][1] += i[1]
                playsBygenres[j][2] += 1
            else:
                j += 1
                playsBygenres[j] = [i[0], i[1], 1]
    totalList.sort(key=lambda x: (-x[1], x[2]))
    playsBygenres.sort(key=lambda x:-x[1])
    j = 0
    cnt = 0

    print(playsBygenres)
    print(totalList)

    while (j < len(playsBygenres)):
        j_ctn = 0
        for i in totalList:
            if i[0] == playsBygenres[j][0]:
                answer.append(i[2])
                j_ctn += 1
                if j_ctn == 2 or playsBygenres[j][2] == 1:
                    j_ctn = 0
                    j += 1
                    break
    return answer






# def solution(genres, plays):
#     answer = []

#     # tmp = [genres, plays]
#     dict = {key:val for key,val in zip(genres, plays)}

#     print(dict)
#     for i in dict:
#         dict[i]

#     return answer



# ==================================================================
# ========================skim's zzangzzangman?=====================
# ==================================================================


# def solution(genres, plays):
#     al_g = dict()
#     al_p = dict()
#     for i in range(len(genres)):
#         if genres[i] in al_g:
#             al_g[genres[i]].append([plays[i], i])
#             al_p[genres[i]] += plays[i]
#         else:
#             al_g[genres[i]] = [[plays[i], i]]
#             al_p[genres[i]] = plays[i]
#     al_p = sorted(al_p.items(), key=lambda x: x[1], reverse=True)
#     answer = []
#     for p in al_p:
#         al_g[p[0]] = sorted(al_g[p[0]], key=lambda a: (-a[0], a[1]))
#         answer.append(al_g[p[0]][0][1])
#         if len(al_g[p[0]]) >= 2:
#             answer.append(al_g[p[0]][1][1])
#     return answer

# ==================================================================
# ==================================================================
# ==================================================================
