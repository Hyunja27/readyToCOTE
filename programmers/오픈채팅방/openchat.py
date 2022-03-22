
def solution(record):
    rt = []
    raw = []
    match = dict()
    leng = len(record)

    for i in record:
        tmp = i.split()
        raw.append(tmp)
        if tmp[0] != "Leave":
            match[tmp[1]] = tmp[2]
    
    for i in raw:
        if (i[0] == "Enter"):
            rt.append(match[i[1]] + "님이 들어왔습니다.")
        elif (i[0] == "Leave"):
            rt.append(match[i[1]] + "님이 나갔습니다.")
    return rt