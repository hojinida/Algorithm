s = input()

for i, c in enumerate(s):
    if i != 0 and i % 10 == 0:
        print()
    print(c, end="")
