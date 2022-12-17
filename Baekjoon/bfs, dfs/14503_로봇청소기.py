dxy = {0: (-1, 0), 3: (0, -1), 2: (1, 0), 1: (0, 1)}
n, m = map(int, input().split())
N, M, D = map(int, input().split())

arr = [[i for i in map(int, input().split())] for _ in range(n)]

count = 0
while True:
    flag = True
    # arr[N][M] 0이면 count를 증가시키고 arr[N][M] 2로 변경
    if arr[N][M] == 0:
        count += 1
        arr[N][M] = 2

    for i in range(4):
        # 왼쪽 방향으로 회전
        D = (D + 3) % 4
        # 바라보는 방향의 한 칸 앞이 0이면 전진하고 flag를 활성화
        if arr[N + dxy[D][0]][M + dxy[D][1]] == 0:
            N += dxy[D][0]
            M += dxy[D][1]
            flag = False
            break
    # 플래그가 활성화 되어있지 않은 경우 - 4방향이 모두 전진할 수 없는 경우
    if flag:
        # 후진한 칸이 벽인 경우 종료
        if arr[N - dxy[D][0]][M - dxy[D][1]] == 1:
            break
        # 아닌 경우 후진한 후 계속 진행
        else:
            N -= dxy[D][0]
            M -= dxy[D][1]
print(count)
