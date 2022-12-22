import sys

answer = [int(input()) for _ in range(9)]

maxV = max(answer)
sys.stdout.write(str(maxV)+'\n')
sys.stdout.write(str(answer.index(maxV)+1))
