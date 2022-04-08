
import copy
import sys
from xml.etree.ElementPath import get_parent_map
sys.setrecursionlimit(1000000)

def scoreCheck(a, b):
    global answer
    scoreA = 0
    scoreB = 0
    tmp = 10
    
    for i in range(11):
        if a[i] == b[i] and a[i] == 0:
            continue
        if a[i] >= b[i]:
            scoreA += tmp
        else:
            scoreB += tmp
        tmp -= 1
    # print("a->", a, "apitch: ", scoreA, "rion: ", scoreB)
    # print("b->", b, "apitch: ", scoreA, "rion: ", scoreB, "\n\n")
    
    
    if b == [0,2,2,0,1,0,0,0,0,0,0]:
        print("->", b, "apitch: ", scoreA, "rion: ", scoreB)
    if scoreA < scoreB:
        gap = scoreB - scoreA
        # print("->", b, "apitch: ", scoreA, "rion: ", scoreB)
        if len(answer) == 0:
            answer = b
        else:
            for i in range(len(answer) - 1, 0, -1):
                if answer[i] < b[i]:
                    # print("->", b, "apitch: ", scoreA, "rion: ", scoreB)
                    answer = b
                    return

def search(n, apitch, rion):
    if n == 0:
        scoreCheck(apitch, rion)
        return
    
    tmp = copy.deepcopy(rion)

    for i in range(11):
        tmp[i] += 1
        # print(tmp)
        search(n - 1, apitch, tmp)
        tmp[i] -= 1


def solution(n, info):
    global answer
    global gap 
    gap = 0
    answer = []
    arr = [0] * 11
    
    search(n, info, arr)

    if len(answer) == 0:
        return [-1]
    return answer

k = solution(5, [2,1,1,1,0,0,0,0,0,0,0])

print("=====>", k)