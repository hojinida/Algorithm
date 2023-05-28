day = {0: 'SUN', 1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT'}
cal = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30, 2: 28}


def calDay(x, y):
    d = 0
    for i in range(1, x):
        d += cal[i]
    d += y
    return d


x, y = map(int, input().split())

print(day[calDay(x, y) % 7])
