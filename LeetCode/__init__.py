def solution(score):
    rank = []
    for s in score:
        st = 1
        for i in range(len(rank)):
            if s > score[i]:
                rank[i] += 1
            else:
                st += 1
        rank.append(st)
    return rank


print(solution([82, 75, 98, 63, 40, 10, 140]))
