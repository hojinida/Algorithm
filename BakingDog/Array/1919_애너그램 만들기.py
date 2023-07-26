from collections import Counter

counter1 = Counter(input())
counter2 = Counter(input())

counter1.subtract(counter2)

print(sum(abs(i) for i in counter1.values()))

