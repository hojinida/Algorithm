import sys

s = input()
s = s.upper()

temp = set(s)

result = []
for i in temp:
    result.append(s.count(i))

maxV = max(result)
if result.count(maxV) > 1:
    sys.stdout.write("?")
else:
    temp = list(temp)
    sys.stdout.write(temp[result.index(maxV)])
