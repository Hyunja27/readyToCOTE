col, row = map(int, input().split())
map = []
taste = 10
count = 0

for i in range(col):
    map.append(list(input()))


def draw():
    for i in range(col):
        print(map[i])


def makeIceCake(col_p, row_p, idx):
    map[col_p][row_p] = str(idx)
    if (col_p + 1 < col) and map[col_p + 1][row_p] == "0":
        makeIceCake(col_p + 1, row_p, idx)
    if (row_p + 1 < row) and map[col_p][row_p + 1] == "0":
        makeIceCake(col_p, row_p + 1, idx)


for i in range(col):
    for j in range(row):
       if map[i][j] == '0':
           makeIceCake(i, j, taste)
           taste += 10
           count += 1


draw()

print(count)





