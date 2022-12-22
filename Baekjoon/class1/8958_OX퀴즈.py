import sys

N = int(input())

inputValue = [input() for _ in range(N)]

for s in inputValue:
    score = 0
    beforeValue = ''
    beforeScore = 0
    for i in s:
        if i == 'O':
            if beforeValue == 'O':
                score += beforeScore + 1
            else:
                score+=1
            beforeScore += 1
        else:
            beforeScore=0
        beforeValue = i
    sys.stdout.write(str(score)+'\n')
