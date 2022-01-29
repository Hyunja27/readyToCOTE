from functools import cmp_to_key



# -> cmp_to_key 로 다중 비교식 만드는 법을 꼭 기억 



# 이거는 죽여주는 참고식 답  
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))





#이거는 내답 
# def melong(x, y):
#     if x[1] < y[1]:
#         return -1
#     elif x[1] == y[1]:
#         if x[0] > x[0]:
#             return 1
#         else:
#             return -1
#     else:
#         return 1

def melong(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1

def solution(numbers):
    numbers = list(str(x) for x in numbers)
    # answer = sorted(total)
    answer = sorted(numbers, key=cmp_to_key(melong))
    answer = ''.join(answer)
    if int(answer) == 0:
        return(str(0))
    else:
        return(''.join(answer))




# def solution(numbers):
#     total = []
#     numbers = list(str(x) for x in numbers)
#     for i in numbers:
#         total.append([i, len(i)])
#     # answer = sorted(total)
#     answer = sorted(total, key=lambda x:(-x[1], -len(x), ), reverse=True)
#     print(answer)
                    


# def solution(numbers):
#     tmp = []
#     answer = []
#     k = 10
#     while k <= 1000:
#         numbers.sort(reverse=True)
#         if len(numbers) == 1:
#             tmp.append(numbers[0])
#             numbers.remove(numbers[0])
#         for i in range(len(numbers) - 1, -1, -1):
#             if int(numbers[i] / k) == 0:
#                 tmp.append(numbers[i])
#                 numbers.remove(numbers[i])
#         tmp.sort(reverse=True)
#         for i in tmp:
#             answer.append(str(i))
#         tmp.clear()
#         k = k * 10
#     return ''.join(answer)





# def solution(numbers):
#     tmp = []
#     answer = []
#     k = 10
#     numbers.sort(reverse=True)
#     while k <= 1000:
#         for i in range(len(numbers) - 1, 0, -1):
#             if int(numbers[i] / k) == 0:
#                 print("->", numbers[i])
#                 tmp.append(numbers[i])
#                 numbers.remove(numbers[i])
#         tmp.sort(reverse=True)
#         print(tmp)
#         for i in tmp:
#             answer.append(str(i))
#         tmp.clear()
#         k = k * 10
#     return ''.join(answer)


# def solution(numbers):
#     answer = ''
#     row = []
#     numbers.sort(reverse=True)
#     print(numbers)
#     tmp = 0
#     for i in numbers:
#         if len(str(i)) > 1:
#             tmp = i
#             while(tmp != 0):    
#                 row.append(str(tmp % 10))
#                 tmp = int(tmp / 10);
#         else:
#             row.append(str(i))
#     row.sort(reverse=True)
#     return (''.join(row))