count = int(input())

def func(num):
    global answer
    global target

    if num == target:
        answer+=1
        return

    if num > target:
        return

    func(num+1)
    func(num+2)
    func(num+3)

for _ in range(count):
    answer = 0
    target = int(input())
    func(0)
    print(answer)