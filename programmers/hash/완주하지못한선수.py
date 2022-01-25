import collections

# def solution(participant, completion):

    # 내 처음코드
    # for i in participant:
    #     if i in completion:
    #         completion.remove(i)
    #     else:
    #         return i

    # 내 최종코드
    # participant.sort()
    # completion.sort()
    # completion.append("zzzzzzzzzzzzz")
    # for i in range(len(participant)):
    #     if participant[i] != completion[i]:
    #         return participant[i]
            
# 간지코드

a = ["marina", "josipa", "nikola", "vinko", "filipa"]	
b = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])
    return list(answer.keys())[0]

solution(a, b)

# collections 대박사껀.....