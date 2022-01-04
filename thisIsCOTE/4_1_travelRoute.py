
n = int(input())
plan = input().split()
pos = [1, 1]

for i in plan:
    if i == 'U':
        if pos[0] == 1:
            pass
        else:
            pos[0] += 1
    elif i == 'D':
        if pos[0] == n - 1:
            pass
        else:
            pos[0] += 1
    elif i == 'R':
        if pos[1] == n - 1:
            pass
        else:
            pos[1] += 1
    else:
        if pos[1] == 1:
            pass
        else:
            pos[1] += 1

print(pos[0], pos[1])
    