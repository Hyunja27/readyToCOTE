def solution(array, commands):
    answer = []
    for i in commands:
        a = i[0]
        b = i[1]
        c = i[2]
        tmp = array[a - 1: b]
        tmp.sort()
        answer.append(tmp[c - 1])
    return answer