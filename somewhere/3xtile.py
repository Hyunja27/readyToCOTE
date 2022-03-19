
n = input()

memory = [0] * 31

def dp(N):
    global memory
    if N == 1:
        return 0
    elif N == 2:
        return 3
    if memory[N] == 0:
        memory[N] = dp(N - 1) + 3 * dp(N - 2)
    return memory[N]

print(dp(int(n)))
