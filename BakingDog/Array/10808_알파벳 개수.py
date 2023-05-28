import sys

s = input()

answer = [0] * 26

for i in s:
    answer[ord(i) - 97] += 1

for i in answer:
    sys.stdout.write(str(i) + " ")
