col, row = map(int, input().split())
map = []
for i in range(col):
    map.append(list(input()))

def search(col_p, row_p, step):
    print("->",step, col_p, row_p)
    if col_p + 1 == col and row_p + 1 == row:
        return step
    if col_p + 1 < col and map[col_p + 1][row_p] == "1":
        return search(col_p + 1, row_p, step + 1)
    if row_p + 1 < row and map[col_p][row_p + 1] == "1":
        return search(col_p, row_p + 1, step + 1)

print(map)

rt = search(0, 0, 0)
print(rt)