import sys

n, m = input().split()

n = "".join(reversed(str(n)))
m = "".join(reversed(str(m)))

sys.stdout.write(str(max(int(n), int(m))))
