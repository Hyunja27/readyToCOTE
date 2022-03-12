n, k = map(int, input().split())

i = 0
while n != 1:
    if n % k != 0:
        n -= 1
        i += 1
    else:
        n = n / k
        i += 1
        
print(i)
