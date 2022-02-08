raw,col = map(int, input().split())
raw_pos, col_pos, direct = map(int, (input().split()))




# gameMap = [[0] *raw for i in range(col)]
gameMap = []

print("!! \n")
pos = [raw_pos, col_pos]
print(pos)
for i in range(raw):
    gameMap.append(list(map(int, input().split())))

# print(gameMap[pos[0]][pos[1]])
if gameMap[pos[0]][pos[1]] != 0:
    print("map error")
    exit


elsecount = 0


print('???')
while 1:
    print(pos, " is ", gameMap[pos[0]][pos[1]])
    gameMap[pos[0]][pos[1]] = 2
    if elsecount == 4:
        if direct == 0:
            if gameMap[pos[0] + 1][pos[1]] == 1:
                break
            pos[0] += 1    
        elif direct == 1:
            if gameMap[pos[0]][pos[1] + 1] == 1:
                break
            pos[1] += 1
        elif direct == 2:
            if gameMap[pos[0] - 1][pos[1]] == 1:
                break
            pos[0] -= 1
        elif direct == 3:
            if gameMap[pos[0]][pos[1] - 1] == 1:
                break
            pos[1] -= 1
        elsecount = 0
    if direct == 0:
        if gameMap[pos[0]][pos[1] - 1] == 0:
            direct += 1
            pos[1] -= 1
            elsecount = 0
        else:
            direct += 1
            elsecount += 1
    elif direct == 1:
        if gameMap[pos[0] + 1][pos[1]] == 0:
            direct += 1
            pos[0] += 1
            elsecount = 0
        else:
            direct += 1
            elsecount += 1
    
    elif direct == 2:
        if gameMap[pos[0]][pos[1] + 1] == 0:
            direct += 1
            pos[1] += 1
            elsecount = 0
        else:
            direct += 1
            elsecount += 1
    elif direct == 3:
        if gameMap[pos[0] - 1][pos[1]] == 0:
            direct = 0
            pos[0] -= 1
            elsecount = 0
        else:
                direct = 0
                elsecount += 1
        # if elsecount == 4:
        #     if direct == 0:
        #         if gameMap[pos[0] + 1][pos[1]] == 1:
        #             break
        #         pos[0] += 1    
        #     elif direct == 1:
        #         if gameMap[pos[0]][pos[1] + 1] == 1:
        #             break
        #         pos[1] += 1
        #     elif direct == 2:
        #         if gameMap[pos[0] - 1][pos[1]] == 1:
        #             break
        #         pos[0] -= 1
        #     elif direct == 3:
        #         if gameMap[pos[0]][pos[1] - 1] == 1:
        #             break
        #         pos[1] -= 1
        #     elsecount = 0

print(gameMap)

# 이제 2차원 배열 안에 있는 2만 체크하면 될듯!
elsecount = 0
for i in range(raw):
    for j in range(col):
        if gameMap[i][j] == 2:
            elsecount += 1

print("Answer is ", elsecount)

