# 20055_컨베이어 벨트 위의 로봇_conveyorRobot
# 푸는중
import sys
from collections import deque
# input = sys.stdin.readline

N, K = map(int, input().split())

conveyor = list(map(int, input().split()))

conve1 = deque()
conve2 = deque()
for i in range(N):
    conve1.append([conveyor[i], 0])
for j in range(N, 2*N):
    conve2.appendleft([conveyor[j], 0])

cnt = 0
ans = 0

while True:
    # 단계 4
    if cnt >= K:
        break
    ans += 1

    # 단계1
    temp1 = conve2.popleft()
    temp2 = conve1.pop()

    conve1.appendleft(temp1)
    conve2.append(temp2)
    # 단계2
    for i in range(N-2,-1,-1):
        if conve1[i+1][1] == 0 and conve1[i][1] == 1:
            conve1[i][1] = 0
            conve1[i+1][1] = 1
            conve1[i+1][0] -= 1
            if conve1[i+1][0] == 0:
                cnt += 1
    conve1[N-1][1] = 0
    # 단계3
    if conve1[0][0] != 0:
        conve1[0][1] = 1

print(ans)
