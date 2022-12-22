import sys

sys.stdout.write(str(len(set([int(input()) % 42 for _ in range(10)]))))
