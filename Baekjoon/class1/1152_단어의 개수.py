import sys

s = input()
answer = s.split(" ", )

count = 0
for i in answer:
    if '' != i:
        count += 1

sys.stdout.write(str(count))
