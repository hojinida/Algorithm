def solution(sides):
    answer = 0
    maxIndex = 0
    for i in range(1,len(sides)):
        if sides[i] > sides[maxIndex]:
            maxIndex = i
            
    value = 0
    for i in range(len(sides)):
        if i != maxIndex:
            value += sides[i]
    
    if sides[maxIndex] >= value:
        return 2
    return 1