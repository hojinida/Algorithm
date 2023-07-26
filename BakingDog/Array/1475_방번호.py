s = input()

counter = [0] * 10

for i in range(len(s)):
    counter[int(s[i])] += 1
counter[6] = (counter[6] + counter[9] + 1) // 2
counter[9] = 0

print(max(counter))
