import sys

s = input()
s=s.upper()

temp = set(s)


answer = 0
result=''

for i in temp:
    count = s.count(i)
    if answer == count:
        sys.stdout.write("?")
        exit(0)
    if answer < count:
        answer = count
        result = i

sys.stdout.write(result)
