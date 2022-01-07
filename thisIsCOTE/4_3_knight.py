raw = input()
col = raw[0] 
row = int(raw[1])
col_idx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row_idx = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0

if col_idx.index(col) + 2 <= 7:
        if row_idx.index(row) + 2 <= 7:
            count += 1
        if row_idx.index(row) - 2 >= 0:
            count += 1
if col_idx.index(col) -2 >= 0:
        if row_idx.index(row) + 2 <= 7:
            count += 1
        if row_idx.index(row) - 2 >= 0:
            count += 1
if row_idx.index(row) + 2 <= 7:
        if col_idx.index(col) + 2 <= 7:
            count += 1
        if col_idx.index(col) - 2 >= 0:
            count += 1
if row_idx.index(row) -2 >= 0:
        if col_idx.index(col) + 2 <= 7:
            count += 1
        if col_idx.index(col) - 2 >= 0:
            count += 1

print(count)