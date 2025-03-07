from collections import defaultdict
def solution(clothes):
    pattern = defaultdict(list)
    for clothe in clothes:
        pattern[clothe[1]].append(clothe[0])
    answer = 1
 
    for i in pattern.values():
        answer*= (len(i)+1)
    return answer -1 