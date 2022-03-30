# 모의고사
# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
# 입출력 예 설명
# 입출력 예 #1



# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

#싀킴정답

def solution(answers):
    num_one = [1, 2, 3, 4, 5]
    num_two = [2, 1, 2, 3, 2, 4, 2, 5]
    num_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_len = len(num_one)
    two_len = len(num_two)
    three_len = len(num_three)
    answer = [0, 0, 0]
    for i in range(0, len(answers)):
        if answers[i] == num_one[i % one_len]:
            answer[0] += 1
        if answers[i] == num_two[i % two_len]:
            answer[1] += 1
        if answers[i] == num_three[i % three_len]:
            answer[2] += 1
    answer = [i + 1 for i, value in enumerate(answer) if value == max(answer)]
    return answer



# 내 정답

def solution(answers):
    rt = [0] * 3
    a = []
    cases = [[],[],[]] 
    count = 0
    
    cases[0] = [i % 5 + 1 for i in range(len(answers))]
    for i in range(len(answers)):
        if int(i % 2) == 0:
            cases[1].append(2)
        else:
            if count == 0:
                cases[1].append(1)
            elif count == 1:
                cases[1].append(3)
            elif count == 2:
                cases[1].append(4)
            elif count == 3:
                cases[1].append(5)
            count += 1
            if count == 4:
                count = 0
    count = 0
    for i in range(len(answers)):
        if count == 0 or count == 1:
            cases[2].append(3)
        elif count == 2 or count == 3:
            cases[2].append(1)
        elif count == 4 or count == 5:
            cases[2].append(2)
        elif count == 6 or count == 7:
            cases[2].append(4)
        elif count == 8 or count == 9:
            cases[2].append(5)
        count += 1
        if count == 10:
            count = 0
    count = 0
    for i in answers:
        if i == cases[0][count]:
            rt[0] += 1
        if i == cases[1][count]:
            rt[1] += 1
        if i == cases[2][count]:
            rt[2] += 1
        count += 1
    for p, v in enumerate(rt): 
        if v == max(rt):
            a.append(p + 1)
    return (a)