raw,col = map(int, input().split())
raw_pos, col_pos, direct = map(int, (input().split()))

# gameMap = [[0] *raw for i in range(col)]
gameMap = []

for i in range(raw):
   gameMap.append(input().split())

pos = [raw, col]

if gameMap[pos[0]][pos[1]] != 0:
    print("map error")
    exit

elsecount = 0

while 1:
    if gameMap[pos[0]][pos[1]] == 0:
        gameMap[pos[0]][pos[1]] = 2
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

# 이제 2차원 배열 안에 있는 2만 체크하면 될듯!
# for i in range

